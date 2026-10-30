import os
from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = "Earth Information Jukebox API"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./earth_jukebox.db")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "earth-jukebox-super-secret-key-32chars-min!")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "*"
    ]

settings = Settings()
