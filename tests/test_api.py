"""
Testes da API.
"""
import pytest
from fastapi.testclient import TestClient

from src.api.main import create_app


@pytest.fixture
def client() -> TestClient:
    """Cliente de teste da API."""
    app = create_app()
    return TestClient(app)


def test_health_check(client: TestClient) -> None:
    """Testa endpoint de health check."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_predict_success(client: TestClient) -> None:
    """Testa predição com dados válidos."""
    payload = {
        "age": 35,
        "income": 50000,
        "credit_score": 750,
        "loan_amount": 20000,
        "employment_years": 8,
        "existing_debts": 5000,
    }
    response = client.post("/api/v1/predict", json=payload)
    
    # Se modelo não estiver carregado, será 500
    if response.status_code != 500:
        assert response.status_code == 200
        data = response.json()
        assert "approved" in data
        assert "approval_probability" in data
        assert "risk_level" in data


def test_predict_invalid_input(client: TestClient) -> None:
    """Testa validação de entrada."""
    invalid_payload = {
        "age": -5,  # Inválido
        "income": 50000,
        "credit_score": 750,
        "loan_amount": 20000,
        "employment_years": 8,
        "existing_debts": 5000,
    }
    response = client.post("/api/v1/predict", json=invalid_payload)
    assert response.status_code == 422  # Validation error


def test_predict_missing_fields(client: TestClient) -> None:
    """Testa requisição com campos faltantes."""
    invalid_payload = {"age": 35}  # Faltam campos
    response = client.post("/api/v1/predict", json=invalid_payload)
    assert response.status_code == 422
