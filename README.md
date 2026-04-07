# Credit Approval ML API

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)

**REST API for credit approval prediction** using Machine Learning with FastAPI, with professional code patterns, logging, environment-based configuration, and Docker support.

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
# Linux/Mac (via Makefile)
make install

# Or manually on any platform
pip install -r requirements.txt
pip install -e ".[dev]"       # editable mode (makes imports work everywhere)
```

> **Windows tip:** Run `setup.bat` to do all setup automatically.

### 4. Configure environment variables

```bash
# Copy example file
cp .env.example .env

# Edit .env with your settings (optional)
```

## 🤖 Model Training

The script generates synthetic data, trains the model, and serializes it:

```bash
# Linux/Mac
make train-model

# Windows (without PYTHONPATH issues)
python -c "from scripts.train_model import main; main()"
```

**Expected output:**
- `models_trained/credit_model.pkl` (Random Forest model)
- `models_trained/scaler.pkl` (StandardScaler)
- Accuracy and metrics log

## ▶️ Running Locally

### Development Mode

```bash
# Linux/Mac
make run

# Windows
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
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

### Build the Image

```bash
make docker-build
```

### Run Container

```bash
make docker-run
```

API will be at: http://localhost:8000

### Stop Containers

```bash
make docker-stop
```

## 🔌 API Endpoints

### GET `/api/v1/health`

Health check and model status.

**Response:**

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "model_loaded": true
}
```

### POST `/api/v1/predict`

Predict credit approval.

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

**Validation:**
- `age`: 0 < age ≤ 100
- `income`: income > 0
- `credit_score`: 0 ≤ score ≤ 1000
- `loan_amount`: loan > 0
- `employment_years`: 0 ≤ years ≤ 60
- `existing_debts`: debts ≥ 0

## ✅ Testing

### Run all tests

```bash
make test
```

### Tests with coverage

```bash
make test-cov
```

Report at: `htmlcov/index.html`

### Specific tests

```bash
pytest tests/test_api.py -v
```

## 📐 Code Patterns

### 1. **Type Hints**

All modules use complete type hints:

```python
def predict(self, X: pd.DataFrame) -> np.ndarray:
    """Perform prediction."""
    pass
```

### 2. **Structured Logging**

JSON logs with full context:

```python
logger = get_logger(__name__)
logger.info(f"Model trained. Accuracy: {accuracy:.4f}")
```

### 3. **Configuration via Environment**

Variables via `.env` using `pydantic-settings`:

```python
from src.utils.config import get_settings

settings = get_settings()
print(settings.api_port)  # 8000
```

### 4. **Validation with Pydantic**

Automatic schemas and validation:

```python
class PredictionRequest(BaseModel):
    age: float = Field(..., gt=0, le=100)
```

### 5. **Dependency Injection**

FastAPI dependencies pattern:

```python
@app.post("/predict")
async def predict(
    request: PredictionRequest,
    model: CreditApprovalModel = Depends(get_model),
):
    pass
```

### 6. **English Docstrings**

Clear documentation with complete examples:

```python
def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> dict:
    """
    Train the classification model.
    
    Args:
        X_train: Training features
        y_train: Training target
    
    Returns:
        Training metrics
    """
    pass
```

## 🛠️ Makefile Commands

```bash
make help           # Show all commands
make install        # Install dependencies
make train-model    # Train the model
make run            # Execute API locally
make test           # Run tests
make test-cov       # Tests with coverage
make docker-build   # Build Docker
make docker-run     # Run Docker
make clean          # Clean temporary files
make format         # Format code
make lint           # Linting
```

## 📊 Model Structure

**Type:** Random Forest Classifier
- **Estimators:** 100 trees
- **Max Depth:** 10
- **Normalization:** StandardScaler

**Features:**
- `age`: Customer age
- `income`: Annual income
- `credit_score`: Credit score
- `loan_amount`: Requested amount
- `employment_years`: Years of employment
- `existing_debts`: Existing debts

## 📝 License

MIT

## 👤 Author

Rubens Rudio
