# Credit Approval ML API

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)

Projeto de portfólio: **API REST para predição de aprovação de crédito** usando Machine Learning com FastAPI, com padrões profissionais de código, logging, config via variáveis de ambiente e suporte a Docker.

## 📋 Índice

- [Arquitetura](#arquitetura)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Treinamento](#treinamento)
- [Execução](#execução)
- [Docker](#docker)
- [API](#api)
- [Testes](#testes)
- [Padrões de Código](#padrões-de-código)

## 🏗️ Arquitetura

```
credit-approval-ml-api/
├── src/                          # Código-fonte principal
│   ├── api/                      # API FastAPI
│   │   ├── main.py              # App principal
│   │   ├── routes.py            # Rotas
│   │   ├── schemas.py           # Schemas Pydantic
│   │   └── dependencies.py      # Injeção de dependências
│   ├── models/                   # Modelos ML
│   │   └── credit_model.py      # Classificador de crédito
│   └── utils/                    # Utilitários
│       ├── config.py            # Configurações (env)
│       ├── logger.py            # Logging estruturado
│       └── __init__.py
│
├── notebooks/                    # Jupyter Notebooks
│   └── exploration.ipynb        # EDA e treinamento
│
├── tests/                        # Testes
│   ├── test_api.py             # Testes da API
│   └── __init__.py
│
├── scripts/                      # Scripts utilitários
│   └── train_model.py           # Treinamento do modelo
│
├── data/                         # Dados (não versionados)
│   ├── raw/                     # Dados brutos
│   └── processed/               # Dados processados
│
├── models_trained/               # Modelos treinados
│   ├── credit_model.pkl         # Modelo serializado
│   └── scaler.pkl               # StandardScaler
│
├── docker/                       # Arquivos Docker
│   └── Dockerfile
│
├── logs/                         # Logs (não versionado)
│
├── docker-compose.yml           # Docker Compose
├── Makefile                     # Automação
├── requirements.txt             # Dependências Python
├── .env.example                 # Exemplo de variáveis de ambiente
├── .gitignore                   # Git ignore
└── README.md                    # Este arquivo
```

## 📋 Checklist de Desenvolvimento

- [ ] **Fase 1: Setup**
  - [ ] Clonar repositório
  - [ ] Criar ambiente virtualenv
  - [ ] Instalar dependências (`make install`)
  - [ ] Configurar `.env`

- [ ] **Fase 2: Modelagem**
  - [ ] Exploração de dados (notebook)
  - [ ] Feature engineering
  - [ ] Treinamento do modelo (`make train-model`)
  - [ ] Avaliação e validação
  - [ ] Serializar modelo em pickle

- [ ] **Fase 3: API**
  - [ ] Implementar schemas Pydantic (validação)
  - [ ] Implementar rotas REST
  - [ ] Adicionar health check
  - [ ] Logging estruturado
  - [ ] Tratamento de erros

- [ ] **Fase 4: Testes**
  - [ ] Testes unitários
  - [ ] Testes de integração
  - [ ] Testes com client TestClient (FastAPI)
  - [ ] Cobertura de código (`make test-cov`)

- [ ] **Fase 5: Docker**
  - [ ] Criar Dockerfile
  - [ ] Criar docker-compose.yml
  - [ ] Testar build (`make docker-build`)
  - [ ] Testar run (`make docker-run`)
  - [ ] Health checks

- [ ] **Fase 6: Qualidade**
  - [ ] Linting (`make lint`)
  - [ ] Type hints (mypy)
  - [ ] Formatação (`make format`)
  - [ ] Documentação de código
  - [ ] Docstrings em português

- [ ] **Fase 7: Deploy (opcional)**
  - [ ] Preparar para Heroku/Railway
  - [ ] Guarder secrets com segurança
  - [ ] CI/CD pipeline (GitHub Actions)

## 🔧 Pré-requisitos

- Python 3.11+
- pip ou conda
- Docker e Docker Compose (opcional)
- Git

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/credit-approval-ml-api.git
cd credit-approval-ml-api
```

### 2. Criar ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
make install
```

Ou manualmente:

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env com suas configurações (opcional)
```

## 🤖 Treinamento do Modelo

O script gera dados sintéticos, treina o modelo e o serializa:

```bash
make train-model
```

Ou:

```bash
python scripts/train_model.py
```

**Output esperado:**
- `models_trained/credit_model.pkl` (modelo Random Forest)
- `models_trained/scaler.pkl` (StandardScaler)
- Log de acurácia e métricas

## ▶️ Execução Local

### Modo Desenvolvimento

```bash
make run
```

A API estará disponível em:
- **API**: http://localhost:8000
- **Docs Swagger**: http://localhost:8000/docs
- **Docs ReDoc**: http://localhost:8000/redoc

### Exemplo de Requisição

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

**Response esperada:**

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

Seu Nome - Portfolio Project

---

**Desenvolvido com ❤️ para demonstrar padrões profissionais de ML + API**
