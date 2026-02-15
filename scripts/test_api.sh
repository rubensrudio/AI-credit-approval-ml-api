#!/bin/bash
# Exemplos de teste da API using CURL
# Use estes comandos para testar a API

API_URL="http://localhost:8000/api/v1"

echo "================================================"
echo "Credit Approval ML API - Exemplos CURL"
echo "================================================"
echo ""
echo "PRÉ-REQUISITO: API rodando em http://localhost:8000"
echo "Inicie com: make run"
echo ""

# Health Check
echo "1. Health Check"
echo "================================================"
echo "Comando:"
echo "curl -s $API_URL/health | jq"
echo ""
echo "Response:"
curl -s $API_URL/health | jq
echo ""
echo ""

# Predict - Cliente Aprovado
echo "2. Predição - Cliente com Bom Perfil (Esperado: APROVADO)"
echo "================================================"
echo "Comando:"
echo 'curl -X POST "$API_URL/predict" \\
  -H "Content-Type: application/json" \\
  -d "{
    \"age\": 35,
    \"income\": 50000,
    \"credit_score\": 750,
    \"loan_amount\": 20000,
    \"employment_years\": 8,
    \"existing_debts\": 5000
  }" | jq'
echo ""
echo "Response:"
curl -s -X POST "$API_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "income": 50000,
    "credit_score": 750,
    "loan_amount": 20000,
    "employment_years": 8,
    "existing_debts": 5000
  }' | jq
echo ""
echo ""

# Predict - Cliente Reprovado
echo "3. Predição - Cliente com Risco Alto (Esperado: REPROVADO)"
echo "================================================"
echo "Comando:"
echo 'curl -X POST "$API_URL/predict" \\
  -H "Content-Type: application/json" \\
  -d "{
    \"age\": 25,
    \"income\": 25000,
    \"credit_score\": 550,
    \"loan_amount\": 30000,
    \"employment_years\": 1,
    \"existing_debts\": 15000
  }" | jq'
echo ""
echo "Response:"
curl -s -X POST "$API_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 25,
    "income": 25000,
    "credit_score": 550,
    "loan_amount": 30000,
    "employment_years": 1,
    "existing_debts": 15000
  }' | jq
echo ""
echo ""

# Predict - Cliente Premium
echo "4. Predição - Cliente Premium (Esperado: APROVADO, Risco Baixo)"
echo "================================================"
echo "Comando:"
echo 'curl -X POST "$API_URL/predict" \\
  -H "Content-Type: application/json" \\
  -d "{
    \"age\": 45,
    \"income\": 100000,
    \"credit_score\": 820,
    \"loan_amount\": 50000,
    \"employment_years\": 20,
    \"existing_debts\": 0
  }" | jq'
echo ""
echo "Response:"
curl -s -X POST "$API_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45,
    "income": 100000,
    "credit_score": 820,
    "loan_amount": 50000,
    "employment_years": 20,
    "existing_debts": 0
  }' | jq
echo ""
echo ""

# Test Validation Error
echo "5. Teste de Validação - Idade Inválida (Esperado: 422)"
echo "================================================"
echo "Comando:"
echo 'curl -s -w "\nStatus: %{http_code}\n" -X POST "$API_URL/predict" \\
  -H "Content-Type: application/json" \\
  -d "{
    \"age\": -5,
    \"income\": 50000,
    \"credit_score\": 750,
    \"loan_amount\": 20000,
    \"employment_years\": 8,
    \"existing_debts\": 5000
  }" | jq'
echo ""
echo "Response:"
curl -s -w "\nStatus: %{http_code}\n" -X POST "$API_URL/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": -5,
    "income": 50000,
    "credit_score": 750,
    "loan_amount": 20000,
    "employment_years": 8,
    "existing_debts": 5000
  }' | jq
echo ""
echo ""

echo "================================================"
echo "✓ Testes Completados!"
echo "================================================"
echo ""
echo "Documentação Interativa (FastAPI):"
echo "- Swagger UI: http://localhost:8000/docs"
echo "- ReDoc: http://localhost:8000/redoc"
echo ""
echo "Para mais informações, veja README.md"
