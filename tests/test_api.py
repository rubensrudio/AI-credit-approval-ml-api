"""
API tests.
"""
from unittest.mock import MagicMock, patch

import numpy as np
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def mock_model():
    """Mock trained model for testing."""
    model = MagicMock()
    model.predict.return_value = np.array([1])
    model.predict_proba.return_value = np.array([[0.15, 0.85]])
    return model


@pytest.fixture
def client(mock_model) -> TestClient:
    """API test client with mocked model."""
    with patch("src.api.dependencies._model_instance", mock_model):
        with patch("src.api.dependencies.get_model", return_value=mock_model):
            from src.api.main import create_app

            app = create_app()
            return TestClient(app)


def test_health_check(client: TestClient) -> None:
    """Test health check endpoint."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_predict_success(client: TestClient) -> None:
    """Test prediction with valid data."""
    payload = {
        "age": 35,
        "income": 50000,
        "credit_score": 750,
        "loan_amount": 20000,
        "employment_years": 8,
        "existing_debts": 5000,
    }
    response = client.post("/api/v1/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "approved" in data
    assert "approval_probability" in data
    assert "risk_level" in data
    assert data["approved"] is True
    assert data["approval_probability"] == 0.85
    assert data["risk_level"] == "low"


def test_predict_high_risk(client: TestClient) -> None:
    """Test prediction with high-risk profile."""
    with patch("src.api.dependencies._model_instance") as mock:
        mock.predict.return_value = np.array([0])
        mock.predict_proba.return_value = np.array([[0.83, 0.17]])

        with patch("src.api.dependencies.get_model", return_value=mock):
            payload = {
                "age": 25,
                "income": 25000,
                "credit_score": 550,
                "loan_amount": 30000,
                "employment_years": 1,
                "existing_debts": 15000,
            }
            response = client.post("/api/v1/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["approved"] is False
    assert data["risk_level"] == "high"


def test_predict_medium_risk(client: TestClient) -> None:
    """Test prediction with medium-risk profile."""
    with patch("src.api.dependencies._model_instance") as mock:
        mock.predict.return_value = np.array([1])
        mock.predict_proba.return_value = np.array([[0.35, 0.65]])

        with patch("src.api.dependencies.get_model", return_value=mock):
            payload = {
                "age": 30,
                "income": 40000,
                "credit_score": 680,
                "loan_amount": 25000,
                "employment_years": 3,
                "existing_debts": 8000,
            }
            response = client.post("/api/v1/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["approved"] is True
    assert data["risk_level"] == "medium"


def test_predict_invalid_input(client: TestClient) -> None:
    """Test input validation."""
    invalid_payload = {
        "age": -5,  # Invalid
        "income": 50000,
        "credit_score": 750,
        "loan_amount": 20000,
        "employment_years": 8,
        "existing_debts": 5000,
    }
    response = client.post("/api/v1/predict", json=invalid_payload)
    assert response.status_code == 422  # Validation error


def test_predict_missing_fields(client: TestClient) -> None:
    """Test request with missing fields."""
    invalid_payload = {"age": 35}  # Missing fields
    response = client.post("/api/v1/predict", json=invalid_payload)
    assert response.status_code == 422
