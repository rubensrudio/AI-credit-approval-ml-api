# Project Folder Structure

```
credit-approval-ml-api/
│
├── 📁 src/                            ← Main source code
│   ├── 📁 api/                        ← FastAPI application
│   │   ├── main.py                   ← App factory
│   │   ├── routes.py                 ← Endpoints
│   │   ├── schemas.py                ← Pydantic validation
│   │   ├── dependencies.py           ← Dependency injection
│   │   └── __init__.py
│   │
│   ├── 📁 models/                    ← ML models
│   │   ├── credit_model.py           ← Main classifier
│   │   └── __init__.py
│   │
│   ├── 📁 utils/                     ← Utilities
│   │   ├── config.py                 ← Environment configuration
│   │   ├── logger.py                 ← Structured logging
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── 📁 notebooks/                      ← Jupyter Notebooks
│   ├── exploration.ipynb             ← EDA, training, analysis
│   └── __init__.py
│
├── 📁 tests/                         ← Automated tests
│   ├── test_api.py                   ← API tests
│   └── __init__.py
│
├── 📁 scripts/                       ← Utility scripts
│   ├── train_model.py                ← Train and save model
│   ├── test_api_locally.py           ← Local tests with requests
│   ├── test_api.sh                   ← CURL test examples (bash)
│   └── __init__.py
│
├── 📁 data/                          ← Data (NOT versioned)
│   ├── 📁 raw/                       ← Raw data
│   └── 📁 processed/                 ← Processed data
│
├── 📁 models_trained/                ← Serialized models (NOT versioned)
│   ├── credit_model.pkl              ← RandomForestClassifier
│   └── scaler.pkl                    ← StandardScaler
│
├── 📁 docker/                        ← Docker files
│   └── Dockerfile                    ← Container image
│
├── 📁 logs/                          ← Application logs (NOT versioned)
│   └── app.log
│
├── 📄 docker-compose.yml             ← Docker orchestration
├── 📄 Makefile                       ← Task automation
├── 📄 requirements.txt               ← Python dependencies
├── 📄 pytest.ini                     ← Test configuration
├── 📄 .coveragerc                    ← Code coverage config
├── 📄 pyproject.toml                 ← Tool configuration
├── 📄 .env.example                   ← Environment template
├── 📄 .gitignore                     ← Git ignore
├── 📄 .github/                       ← GitHub workflows (optional)
├── 📄 README.md                      ← Main documentation
├── 📄 CHECKLIST.md                   ← Development checklist
└── 📄 PROJECT_STRUCTURE.md           ← This file
```

## 📌 Main Directory Descriptions

### `src/`
Main application source code, structured as:
- **api/**: FastAPI app, routes, validation schemas
- **models/**: ML logic (training, prediction, serialization)
- **utils/**: Config, logging, and helper functions

### `notebooks/`
Jupyter Notebooks for:
- Data exploration (EDA)
- Hypothesis validation
- Visualizations and analysis
- Training in exploratory environment

### `tests/`
Automated tests:
- Unit tests
- Integration tests
- API tests (TestClient)
- Coverage >80%

### `scripts/`
Utility scripts:
- `train_model.py`: Train and serialize model
- `test_api_locally.py`: Tests with requests library
- `test_api.sh`: CURL test examples

### `docker/`
Containerization:
- Dockerfile with Python 3.11-slim
- Configured health checks
- Environment variables

### `data/` and `models_trained/`
Ignored in Git (.gitignore):
- Raw/processed data
- Trained models in pickle format
- Application logs

## 🚀 Quick Start

```bash
# 1. Install
make install

# 2. Train model
make train-model

# 3. Run API
make run

# 4. Test
make test

# 5. Docker
make docker-run
```

---
**Developed with professional ML + Software Engineering standards**
