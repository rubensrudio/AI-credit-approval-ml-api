"""
Tests for Settings configuration.
"""
import pytest

from src.utils.config import Settings, get_settings


def test_default_settings() -> None:
    """Test default environment values."""
    settings = Settings()
    assert settings.environment == "development"
    assert settings.log_level == "INFO"
    assert settings.api_port == 8000
    assert settings.api_version == "1.0.0"


def test_is_production_property() -> None:
    """Test is_production flag."""
    dev_settings = Settings(environment="development")
    assert not dev_settings.is_production

    prod_settings = Settings(environment="production")
    assert prod_settings.is_production

    uppercase_settings = Settings(environment="PRODUCTION")
    assert uppercase_settings.is_production


def test_allowed_origins_default() -> None:
    """Test default CORS origins."""
    settings = Settings()
    assert settings.allowed_origins == "*"


def test_allowed_origins_custom() -> None:
    """Test custom CORS origins."""
    settings = Settings(allowed_origins="https://myapp.com,https://admin.myapp.com")
    origins = settings.allowed_origins.split(",")
    assert len(origins) == 2
    assert "https://myapp.com" in origins


def test_get_settings_is_cached() -> None:
    """Test get_settings returns consistent singleton."""
    settings1 = get_settings()
    settings2 = get_settings()
    assert settings1 is settings2
