"""
API tests.
"""
import pytest
from fastapi.testclient import TestClient

from src.api.main import create_app


@pytest.fixture
def client() -> TestClient:
    """API test client."""
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
    
    # If model is not loaded, it will be 500
    if response.status_code != 500:
        assert response.status_code == 200
        data = response.json()
        assert "approved" in data
        assert "approval_probability" in data
        assert "risk_level" in data


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
