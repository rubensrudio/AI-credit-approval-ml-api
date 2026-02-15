# Credit Approval ML API

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)

Portfolio project: **REST API for credit approval prediction** using Machine Learning with FastAPI, with professional code patterns, logging, environment-based configuration, and Docker support.

## 📋 Table of Contents

- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Training](#training)
- [Running](#running)
- [Docker](#docker)
- [API](#api)
- [Testing](#testing)
- [Code Patterns](#code-patterns)

## 🏗️ Architecture

```
credit-approval-ml-api/
├── src/                          # Main source code
│   ├── api/                      # FastAPI application
│   │   ├── main.py              # App factory
│   │   ├── routes.py            # Route endpoints
│   │   ├── schemas.py           # Pydantic schemas
│   │   └── dependencies.py      # Dependency injection
│   ├── models/                   # ML models
│   │   └── credit_model.py      # Credit classifier
│   └── utils/                    # Utilities
│       ├── config.py            # Configuration (env)
│       ├── logger.py            # Structured logging
│       └── __init__.py
│
├── notebooks/                    # Jupyter Notebooks
│   └── exploration.ipynb        # EDA and training
│
├── tests/                        # Tests
│   ├── test_api.py             # API tests
│   └── __init__.py
│
├── scripts/                      # Utility scripts
│   └── train_model.py           # Model training
│
├── data/                         # Data (not versioned)
│   ├── raw/                     # Raw data
│   └── processed/               # Processed data
│
├── models_trained/               # Trained models
│   ├── credit_model.pkl         # Serialized model
│   └── scaler.pkl               # StandardScaler
│
├── docker/                       # Docker files
│   └── Dockerfile
│
├── logs/                         # Logs (not versioned)
│
├── docker-compose.yml           # Docker Compose
├── Makefile                     # Task automation
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables example
├── .gitignore                   # Git ignore
└── README.md                    # This file
```

## 📋 Development Checklist

- [ ] **Phase 1: Setup**
  - [ ] Clone repository
  - [ ] Create virtualenv environment
  - [ ] Install dependencies (`make install`)
  - [ ] Configure `.env`

- [ ] **Phase 2: Modeling**
  - [ ] Data exploration (notebook)
  - [ ] Feature engineering
  - [ ] Model training (`make train-model`)
  - [ ] Evaluation and validation
  - [ ] Serialize model to pickle

- [ ] **Phase 3: API**
  - [ ] Implement Pydantic schemas (validation)
  - [ ] Implement REST routes
  - [ ] Add health check
  - [ ] Structured logging
  - [ ] Error handling

- [ ] **Phase 4: Testing**
  - [ ] Unit tests
  - [ ] Integration tests
  - [ ] TestClient tests (FastAPI)
  - [ ] Code coverage (`make test-cov`)

- [ ] **Phase 5: Docker**
  - [ ] Create Dockerfile
  - [ ] Create docker-compose.yml
  - [ ] Test build (`make docker-build`)
  - [ ] Test run (`make docker-run`)
  - [ ] Health checks

- [ ] **Phase 6: Quality**
  - [ ] Linting (`make lint`)
  - [ ] Type hints (mypy)
  - [ ] Formatting (`make format`)
  - [ ] Code documentation
  - [ ] English docstrings

- [ ] **Phase 7: Deployment (optional)**
  - [ ] Prepare for Heroku/Railway
  - [ ] Secure secrets management
  - [ ] CI/CD pipeline (GitHub Actions)

## 🔧 Requirements

- Python 3.11+
- pip or conda
- Docker and Docker Compose (optional)
- Git

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-user/credit-approval-ml-api.git
cd credit-approval-ml-api
```

### 2. Create virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
make install
```

Or manually:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
# Copy example file
cp .env.example .env

# Edit .env with your settings (optional)
```

## 🤖 Model Training

The script generates synthetic data, trains the model, and serializes it:

```bash
make train-model
```

Or:

```bash
python scripts/train_model.py
```

**Expected output:**
- `models_trained/credit_model.pkl` (Random Forest model)
- `models_trained/scaler.pkl` (StandardScaler)
- Accuracy and metrics log

## ▶️ Running Locally

### Development Mode

```bash
make run
```

The API will be available at:
- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Example Request

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "income": 50000,
    "credit_score": 750,
    "loan_amount": 20000,
    "employment_years": 8,
    "existing_debts": 5000
  }'
```

**Expected response:**

```json
{
  "approved": true,
  "approval_probability": 0.87,
  "risk_level": "low"
}
```

## 🐳 Docker

### Build da Imagem

```bash
make docker-build
```

### Executar Container

```bash
make docker-run
```

API estará em: http://localhost:8000

### Parar Containers

```bash
make docker-stop
```

## 🔌 API Endpoints

### GET `/api/v1/health`

Health check e status do modelo.

**Response:**

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "model_loaded": true
}
```

### POST `/api/v1/predict`

Prediz aprovação de crédito.

**Request:**

```json
{
  "age": 35,
  "income": 50000,
  "credit_score": 750,
  "loan_amount": 20000,
  "employment_years": 8,
  "existing_debts": 5000
}
```

**Response:**

```json
{
  "approved": true,
  "approval_probability": 0.87,
  "risk_level": "low"
}
```

**Validação:**
- `age`: 0 < age ≤ 100
- `income`: income > 0
- `credit_score`: 0 ≤ score ≤ 1000
- `loan_amount`: loan > 0
- `employment_years`: 0 ≤ years ≤ 60
- `existing_debts`: debts ≥ 0

## ✅ Testes

### Rodar todos os testes

```bash
make test
```

### Testes com cobertura

```bash
make test-cov
```

Relatório em: `htmlcov/index.html`

### Testes específicos

```bash
pytest tests/test_api.py -v
```

## 📐 Padrões de Código

### 1. **Type Hints**

Todos os módulos usam type hints completos:

```python
def predict(self, X: pd.DataFrame) -> np.ndarray:
    """Realiza predição."""
    pass
```

### 2. **Logging Estruturado**

Logs em JSON com contexto completo:

```python
logger = get_logger(__name__)
logger.info(f"Modelo treinado. Acurácia: {accuracy:.4f}")
```

### 3. **Configuração via Ambiente**

Variáveis via `.env` usando `pydantic-settings`:

```python
from src.utils.config import get_settings

settings = get_settings()
print(settings.api_port)  # 8000
```

### 4. **Validação com Pydantic**

Schemas automáticos e validação:

```python
class PredictionRequest(BaseModel):
    age: float = Field(..., gt=0, le=100)
```

### 5. **Injeção de Dependências**

FastAPI dependencies pattern:

```python
@app.post("/predict")
async def predict(
    request: PredictionRequest,
    model: CreditApprovalModel = Depends(get_model),
):
    pass
```

### 6. **Docstrings em Português**

Documentação clara e em PT-BR:

```python
def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> dict:
    """
    Treina o modelo de classificação.
    
    Args:
        X_train: Features de treino
        y_train: Target de treino
    
    Returns:
        Métricas de treinamento
    """
    pass
```

## 🛠️ Makefile Commands

```bash
make help           # Mostra todos os comandos
make install        # Instala dependências
make train-model    # Treina o modelo
make run            # Executa API localmente
make test           # Roda testes
make test-cov       # Testes com cobertura
make docker-build   # Compila Docker
make docker-run     # Executa Docker
make clean          # Limpa arquivos temporários
make format         # Formata código
make lint           # Linting
```

## 📊 Estrutura do Modelo

**Tipo:** Random Forest Classifier
- **Estimators:** 100 árvores
- **Max Depth:** 10
- **Normalização:** StandardScaler

**Features:**
- `age`: Idade do cliente
- `income`: Renda anual
- `credit_score`: Score de crédito
- `loan_amount`: Valor solicitado
- `employment_years`: Anos de emprego
- `existing_debts`: Débitos existentes

## 📝 Licença

MIT

## 👤 Autor

Rubens Rudio - Portfolio Project
