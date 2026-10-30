import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings

client = TestClient(app)

def test_cors_policy():
    """Verifies that CORS origins are strictly controlled and not wildcard '*' in headers"""
    response = client.options(
        "/api/quiz/levels",
        headers={
            "Origin": "https://the-earth-information-jukebox.vercel.app",
            "Access-Control-Request-Method": "GET"
        }
    )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "https://the-earth-information-jukebox.vercel.app"

def test_security_headers_present():
    """Verifies defensive HTTP security headers"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers.get("X-Content-Type-Options") == "nosniff"
    assert response.headers.get("X-Frame-Options") == "SAMEORIGIN"
    assert response.headers.get("X-XSS-Protection") == "1; mode=block"

def test_protected_admin_endpoints():
    """Unauthenticated requests to admin audit logs must be rejected with HTTP 403"""
    unauth_resp = client.get("/api/admin/audit-logs")
    assert unauth_resp.status_code == 403
    assert "Forbidden" in unauth_resp.json()["detail"]

    # Authorized request with proper X-Admin-Key succeeds
    auth_resp = client.get("/api/admin/audit-logs", headers={"X-Admin-Key": settings.ADMIN_API_KEY})
    assert auth_resp.status_code == 200
    assert isinstance(auth_resp.json(), list)

def test_server_side_quiz_cheat_protection():
    """Pre-submission questions payload must NOT expose correct answers or explanations"""
    res = client.get("/api/quiz/level/1")
    assert res.status_code == 200
    data = res.json()
    assert len(data["questions"]) == 10
    for q in data["questions"]:
        assert "correct" not in q, "Security vulnerability: Answer key leaked to frontend client!"
        assert "explanationEn" not in q, "Security vulnerability: Explanations leaked before answering!"

def test_quiz_server_grading_integrity():
    """Scoring is enforced by the server, not manipulable by client"""
    sub_res = client.post("/api/quiz/submit", json={
        "level": 1,
        "answers": {
            "1": 1, # Correct (oblate spheroid)
            "2": 1, # Correct (71%)
            "3": 2  # Correct (Earth is 3rd)
        },
        "username": "security_tester"
    })
    assert sub_res.status_code == 200
    result = sub_res.json()
    assert result["score"] == 3
    assert result["passed"] is False # Passing requires 7/10
