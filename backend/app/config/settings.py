import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str 
    DEBUG: bool = False

    # API
    API_V1_PREFIX: str = "/api"
    PROJECT_NAME: str = "BloodConnect"
    PROJECT_VERSION: str = "0.1.0"

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    EMAIL_FROM: str

    FRONTEND_URL: str 

    # CORS
    ALLOWED_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="forbid", 
    )

settings = Settings()
