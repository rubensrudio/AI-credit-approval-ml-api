"""
Exemplos de teste da API usando requests.
Execute com: python scripts/test_api_locally.py
"""
import json
import requests

BASE_URL = "http://localhost:8000/api/v1"

def test_health_check() -> None:
    """Testa endpoint de health check."""
    print("\n" + "=" * 60)
    print("TEST: Health Check")
    print("=" * 60)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✓ PASSOU")


def test_predict_approved() -> None:
    """Testa predição de cliente aprovado."""
    print("\n" + "=" * 60)
    print("TEST: Predict - Candidato com bom perfil (esperado: APROVADO)")
    print("=" * 60)
    
    payload = {
        "age": 35,
        "income": 50000,
        "credit_score": 750,
        "loan_amount": 20000,
        "employment_years": 8,
        "existing_debts": 5000,
    }
    
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    data = response.json()
    assert "approved" in data
    assert "approval_probability" in data
    assert "risk_level" in data
    print("✓ PASSOU")


def test_predict_rejected() -> None:
    """Testa predição de cliente com risco alto."""
    print("\n" + "=" * 60)
    print("TEST: Predict - Candidato com risco alto (esperado: REPROVADO)")
    print("=" * 60)
    
    payload = {
        "age": 25,
        "income": 25000,
        "credit_score": 550,
        "loan_amount": 30000,
        "employment_years": 1,
        "existing_debts": 15000,
    }
    
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    print("✓ PASSOU")


def test_predict_premium() -> None:
    """Testa predição de cliente premium."""
    print("\n" + "=" * 60)
    print("TEST: Predict - Cliente Premium (esperado: APROVADO com baixo risco)")
    print("=" * 60)
    
    payload = {
        "age": 45,
        "income": 100000,
        "credit_score": 820,
        "loan_amount": 50000,
        "employment_years": 20,
        "existing_debts": 0,
    }
    
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["approved"] == True
    assert data["risk_level"] == "low"
    print("✓ PASSOU")


def test_validation_negative_age() -> None:
    """Testa validação - idade negativa."""
    print("\n" + "=" * 60)
    print("TEST: Validation - Idade negativa (esperado: 422)")
    print("=" * 60)
    
    payload = {
        "age": -5,  # Inválido
        "income": 50000,
        "credit_score": 750,
        "loan_amount": 20000,
        "employment_years": 8,
        "existing_debts": 5000,
    }
    
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    
    print(f"Status Code: {response.status_code}")
    
    assert response.status_code == 422
    print("✓ PASSOU - Validação funcionando")


def test_validation_missing_fields() -> None:
    """Testa validação - campos faltando."""
    print("\n" + "=" * 60)
    print("TEST: Validation - Campos faltando (esperado: 422)")
    print("=" * 60)
    
    payload = {
        "age": 35,
        # Faltam outros campos
    }
    
    print(f"Request Payload: {json.dumps(payload, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    
    print(f"Status Code: {response.status_code}")
    
    assert response.status_code == 422
    print("✓ PASSOU - Validação de campos funcionando")


def main() -> None:
    """Executa todos os testes."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + "  TESTES DE API - CREDIT APPROVAL ML API".center(58) + "║")
    print("╚" + "=" * 58 + "╝")
    
    print("\n⚠️ PRÉ-REQUISITO: API deve estar rodando em http://localhost:8000")
    print("   Execute: make run")
    
    try:
        # Test health primeiro
        test_health_check()
        
        # Tests de predição
        test_predict_approved()
        test_predict_rejected()
        test_predict_premium()
        
        # Tests de validação
        test_validation_negative_age()
        test_validation_missing_fields()
        
        print("\n" + "=" * 60)
        print("✓ TODOS OS TESTES PASSARAM!")
        print("=" * 60)
        print("\nAPI está funcionando corretamente! 🚀")
        print("Acesse documentação interativa em:")
        print("  http://localhost:8000/docs (Swagger)")
        print("  http://localhost:8000/redoc (ReDoc)")
        
    except AssertionError as e:
        print(f"\n✗ TESTE FALHOU: {e}")
        exit(1)
    except requests.exceptions.ConnectionError:
        print("\n✗ ERRO DE CONEXÃO")
        print("A API não está rodando em http://localhost:8000")
        print("Execute: make run")
        exit(1)
    except Exception as e:
        print(f"\n✗ ERRO: {e}")
        exit(1)


if __name__ == "__main__":
    main()
