"""
Application configuration module.
"""
from functools import lru_cache
from pydantic_settings import SettingsConfigDict
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration via environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Environment
    environment: str = "development"
    log_level: str = "INFO"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_title: str = "Credit Approval ML API"
    api_version: str = "1.0.0"

    # Security
    allowed_origins: str = Field(
        default="*",
        description="Comma-separated list of allowed CORS origins",
    )

    # Model
    model_path: str = "models_trained/credit_model.pkl"
    scaler_path: str = "models_trained/scaler.pkl"

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"


@lru_cache()
def get_settings() -> Settings:
    """Return singleton instance of Settings."""
    return Settings()
