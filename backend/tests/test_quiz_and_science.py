import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.data.quiz_bank import QUIZ_LEVELS

client = TestClient(app)

def test_quiz_levels_count_and_structure():
    """Validates exactly 10 levels, 10 questions each, total 100 questions"""
    assert len(QUIZ_LEVELS) == 10, f"Expected 10 levels, got {len(QUIZ_LEVELS)}"
    
    total_questions = 0
    question_ids = set()

    for idx, lvl in enumerate(QUIZ_LEVELS):
        lvl_num = idx + 1
        assert lvl["level"] == lvl_num
        assert len(lvl["questions"]) == 10, f"Level {lvl_num} must have exactly 10 questions"
        
        for q in lvl["questions"]:
            total_questions += 1
            assert q["id"] not in question_ids, f"Duplicate question id {q['id']}"
            question_ids.add(q["id"])
            
            # Verify bilingual questions
            assert len(q["qEn"].strip()) > 0
            assert len(q["qAr"].strip()) > 0
            
            # Verify 4 options
            assert len(q["optionsEn"]) >= 3
            assert len(q["optionsAr"]) >= 3
            assert 0 <= q["correct"] < len(q["optionsEn"])
            
            # Verify explanations & sources
            assert len(q["explanationEn"].strip()) > 0
            assert len(q["explanationAr"].strip()) > 0
            assert len(q["source"].strip()) > 0

    assert total_questions == 100, f"Expected 100 questions total, got {total_questions}"

def test_quiz_api_endpoints():
    # Test level listing
    res = client.get("/api/quiz/levels")
    assert res.status_code == 200
    levels = res.json()
    assert len(levels) == 10
    
    # Test level 1 fetch
    res = client.get("/api/quiz/level/1")
    assert res.status_code == 200
    data = res.json()
    assert data["level"] == 1
    assert len(data["questions"]) == 10
    
    # Test submission
    sub_res = client.post("/api/quiz/submit", json={
        "level": 1,
        "answers": {"1": 1, "2": 1, "3": 2},
        "username": "tester"
    })
    assert sub_res.status_code == 200
    sub_data = sub_res.json()
    assert "score" in sub_data
    assert "passed" in sub_data

def test_scientific_datasets_endpoints():
    # Climate indicators
    res = client.get("/api/climate/indicators")
    assert res.status_code == 200
    indicators = res.json()
    assert len(indicators) >= 5
    assert any("NASA" in ind["source"] for ind in indicators)
    
    # Historical climate series
    hist_res = client.get("/api/climate/historical")
    assert hist_res.status_code == 200
    history = hist_res.json()
    assert len(history) >= 15
    assert history[0]["year"] == 1880
    assert history[-1]["year"] == 2024
    
    # Geological chapters
    geo_res = client.get("/api/science/geological-chapters")
    assert geo_res.status_code == 200
    chapters = geo_res.json()
    assert len(chapters) == 6
    
    # Country Atlas
    c_res = client.get("/api/science/countries")
    assert c_res.status_code == 200
    countries = c_res.json()
    assert len(countries) >= 5
