"""
Módulo de configurações da aplicação.
"""
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações da aplicação via variáveis de ambiente."""

    # Environment
    environment: str = "development"
    log_level: str = "INFO"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_title: str = "Credit Approval ML API"
    api_version: str = "1.0.0"

    # Model
    model_path: str = "models_trained/credit_model.pkl"
    scaler_path: str = "models_trained/scaler.pkl"

    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"


@lru_cache()
def get_settings() -> Settings:
    """Retorna instância única de Settings (singleton)."""
    return Settings()
