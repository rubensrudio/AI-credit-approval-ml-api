.PHONY: help install lint format test run docs docker-build docker-run clean

# Variáveis
PYTHON := python
PIP := pip
PORT := 8000
ENV_FILE := .env

help:
	@echo "Credit Approval ML API - Makefile"
	@echo "===================================="
	@echo ""
	@echo "Comandos disponíveis:"
	@echo "  make install        - Instalar dependências"
	@echo "  make train-model    - Treinar modelo ML"
	@echo "  make lint           - Executar linter (flake8, pylint)"
	@echo "  make format         - Formatar código (black, isort)"
	@echo "  make test           - Executar testes"
	@echo "  make test-cov       - Testes com cobertura"
	@echo "  make run            - Rodar API localmente"
	@echo "  make docker-build   - Compilar imagem Docker"
	@echo "  make docker-run     - Rodar via Docker Compose"
	@echo "  make docker-stop    - Parar containers Docker"
	@echo "  make clean          - Limpar arquivos temporários"
	@echo "  make help           - Mostrar este menu"

setup:
	@echo "Configurando ambiente..."
	@if not exist "$(ENV_FILE)" (copy .env.example $(ENV_FILE)) else (echo "$(ENV_FILE) já existe")
	@echo "✓ Arquivo .env criado (revise as variáveis se necessário)"

install: setup
	@echo "Instalando dependências..."
	$(PIP) install -r requirements.txt
	@echo "✓ Dependências instaladas"

train-model:
	@echo "Treinando modelo..."
	$(PYTHON) scripts/train_model.py
	@echo "✓ Modelo treinado"

lint:
	@echo "Executando linter..."
	$(PYTHON) -m pylint src/ --max-line-length=100
	@echo "✓ Lint concluído"

format:
	@echo "Formatando código..."
	$(PYTHON) -m black src/ tests/
	@echo "✓ Código formatado"

test:
	@echo "Executando testes..."
	$(PYTHON) -m pytest tests/ -v
	@echo "✓ Testes concluídos"

test-cov:
	@echo "Executando testes com cobertura..."
	$(PYTHON) -m pytest tests/ -v --cov=src --cov-report=html
	@echo "✓ Cobertura gerada em htmlcov/index.html"

run:
	@echo "Iniciando API em http://localhost:$(PORT)"
	@echo "Docs: http://localhost:$(PORT)/docs"
	uvicorn src.api.main:app --reload --host 0.0.0.0 --port $(PORT)

docker-build:
	@echo "Compilando imagem Docker..."
	docker-compose build
	@echo "✓ Imagem compilada"

docker-run:
	@echo "Iniciando containers Docker..."
	docker-compose up -d
	@echo "✓ Containers iniciados. API em http://localhost:8000"

docker-stop:
	@echo "Parando containers..."
	docker-compose down
	@echo "✓ Containers parados"

clean:
	@echo "Limpando arquivos temporários..."
	@rd /s /q __pycache__ 2>nul || true
	@rd /s /q .pytest_cache 2>nul || true
	@rd /s /q .coverage 2>nul || true
	@rd /s /q htmlcov 2>nul || true
	@del /q *.log 2>nul || true
	@echo "✓ Limpeza concluída"
