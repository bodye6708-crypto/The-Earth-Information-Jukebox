import os
import secrets
from pydantic import BaseModel

class Settings(BaseModel):
    APP_NAME: str = "Earth Information Jukebox API"
    VERSION: str = "1.1.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./earth_jukebox.db")
    
    # Secure secret generation with no hardcoded vulnerable defaults
    JWT_SECRET: str = os.getenv("JWT_SECRET", secrets.token_hex(32))
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    # Strict Admin API Key protection
    ADMIN_API_KEY: str = os.getenv("ADMIN_API_KEY", secrets.token_hex(24))

    # Strict CORS Allowlist (No wildcards in production)
    CORS_ORIGINS: list[str] = [
        origin.strip() for origin in os.getenv(
            "CORS_ORIGINS",
            "https://the-earth-information-jukebox.vercel.app,http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173"
        ).split(",") if origin.strip()
    ]

settings = Settings()
