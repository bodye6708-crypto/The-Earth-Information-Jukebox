import os
import datetime
from fastapi import FastAPI, Depends, HTTPException, Query, Security, status, Header
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

from app.config import settings
from app.database import engine, Base, get_db
from app.models import User, QuizProgress, StoryProgress, AuditLog
from app.data.quiz_bank import QUIZ_LEVELS
from app.data.science_data import (
    CLIMATE_INDICATORS,
    HISTORICAL_CLIMATE_SERIES,
    GEOLOGICAL_CHAPTERS,
    PEER_REVIEWED_PUBLICATIONS,
    COUNTRY_PROFILES
)
from app.data.children_stories import CHILDREN_STORIES

# Initialize Database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend API powering The Earth Information Jukebox with Verified Science",
)

# Strict CORS Allowlist (No wildcard '*' in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# API Security Headers Middleware
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    return response

# Security Dependency for Protected Administrative Operations
api_key_header = APIKeyHeader(name="X-Admin-Key", auto_error=False)

def verify_admin_key(api_key: str = Security(api_key_header)):
    if not api_key or api_key != settings.ADMIN_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Administrative privileges or valid X-Admin-Key required."
        )
    return True

@app.get("/")
def read_root():
    return {
        "message": "Welcome to The Earth Information Jukebox API",
        "version": settings.VERSION,
        "status": "online",
        "verified_science": True
    }

@app.get("/api/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(User.__table__.select().limit(1))
        db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"

    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.VERSION,
        "database": db_status
    }

# ==================== QUIZ SYSTEM ENDPOINTS ====================

@app.get("/api/quiz/levels")
def get_quiz_levels():
    """Returns overview of all 10 levels"""
    return [
        {
            "level": lvl["level"],
            "titleEn": lvl["titleEn"],
            "titleAr": lvl["titleAr"],
            "difficulty": lvl["difficulty"],
            "questionCount": len(lvl["questions"])
        }
        for lvl in QUIZ_LEVELS
    ]

@app.get("/api/quiz/level/{level_num}")
def get_quiz_level_questions(level_num: int):
    """
    Returns all 10 questions for a given level with ANSWER KEYS STRIPPED.
    Defends against cheat inspections before official server-side grading.
    """
    if level_num < 1 or level_num > len(QUIZ_LEVELS):
        raise HTTPException(status_code=404, detail="Quiz level not found. Valid levels are 1 through 10.")
    
    target_lvl = QUIZ_LEVELS[level_num - 1]
    
    # Strip correct answers and explanations from the student pre-submission payload
    sanitized_questions = [
        {
            "id": q["id"],
            "qEn": q["qEn"],
            "qAr": q["qAr"],
            "optionsEn": q["optionsEn"],
            "optionsAr": q["optionsAr"],
            "source": q["source"]
        }
        for q in target_lvl["questions"]
    ]

    return {
        "level": target_lvl["level"],
        "titleEn": target_lvl["titleEn"],
        "titleAr": target_lvl["titleAr"],
        "difficulty": target_lvl["difficulty"],
        "questions": sanitized_questions
    }

class QuizSubmitRequest(BaseModel):
    level: int = Field(..., ge=1, le=10)
    answers: dict[str, int] # question_id (str) -> selected_option (int)
    username: str | None = Field(default="guest", max_length=50)

@app.post("/api/quiz/submit")
def submit_quiz_level(req: QuizSubmitRequest, db: Session = Depends(get_db)):
    if req.level < 1 or req.level > len(QUIZ_LEVELS):
        raise HTTPException(status_code=400, detail="Invalid quiz level")
    
    level_data = QUIZ_LEVELS[req.level - 1]
    total_q = len(level_data["questions"])
    score = 0
    detailed_feedback = []

    for q in level_data["questions"]:
        qid_str = str(q["id"])
        user_choice = req.answers.get(qid_str)
        is_correct = (user_choice == q["correct"])
        if is_correct:
            score += 1
        detailed_feedback.append({
            "id": q["id"],
            "isCorrect": is_correct,
            "correctOption": q["correct"],
            "userChoice": user_choice,
            "explanationEn": q["explanationEn"],
            "explanationAr": q["explanationAr"],
            "source": q["source"]
        })

    passed = (score >= 7) # 70% passing threshold
    
    # Audit logging
    log_entry = AuditLog(
        user_id=None,
        username=req.username,
        event=f"QUIZ_LEVEL_{req.level}_SUBMISSION",
        details=f"Score: {score}/{total_q}, Passed: {passed}"
    )
    db.add(log_entry)
    db.commit()

    return {
        "level": req.level,
        "score": score,
        "total": total_q,
        "passed": passed,
        "nextLevelUnlocked": passed and req.level < 10,
        "feedback": detailed_feedback
    }

# ==================== CLIMATE & SCIENTIFIC OBSERVATIONS ====================

@app.get("/api/climate/indicators")
def get_climate_indicators():
    return CLIMATE_INDICATORS

@app.get("/api/climate/historical")
def get_historical_climate():
    return HISTORICAL_CLIMATE_SERIES

@app.get("/api/science/geological-chapters")
def get_geological_chapters():
    return GEOLOGICAL_CHAPTERS

@app.get("/api/science/publications")
def get_publications(query: str | None = Query(None)):
    if not query:
        return PEER_REVIEWED_PUBLICATIONS
    q = query.lower()
    return [
        p for p in PEER_REVIEWED_PUBLICATIONS
        if q in p["title"].lower() or q in p["authors"].lower() or q in p["journal"].lower()
    ]

@app.get("/api/science/countries")
def get_countries(search: str | None = Query(None)):
    if not search:
        return COUNTRY_PROFILES
    s = search.lower()
    return [
        c for c in COUNTRY_PROFILES
        if s in c["nameEn"].lower() or s in c["nameAr"].lower() or s in c["capital"].lower() or s in c["code"].lower()
    ]

# ==================== CHILDREN STORIES ====================

@app.get("/api/stories")
def get_children_stories():
    return CHILDREN_STORIES

# ==================== AUDIT & ADMIN LOGS (PROTECTED) ====================

@app.get("/api/admin/audit-logs")
def get_audit_logs(
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
    is_admin: bool = Depends(verify_admin_key)
):
    """Protected endpoint requiring X-Admin-Key authorization"""
    logs = db.query(AuditLog).order_by(AuditLog.id.desc()).limit(limit).all()
    return [
        {
            "id": l.id,
            "username": l.username,
            "event": l.event,
            "timestamp": l.timestamp.isoformat() if l.timestamp else None,
            "details": l.details
        }
        for l in logs
    ]
