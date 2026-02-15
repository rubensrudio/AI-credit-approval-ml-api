# Estrutura de Pastas do Projeto

```
credit-approval-ml-api/
│
├── 📁 src/                            ← Código-fonte principal
│   ├── 📁 api/                        ← API FastAPI
│   │   ├── main.py                   ← App factory
│   │   ├── routes.py                 ← Endpoints
│   │   ├── schemas.py                ← Validação Pydantic
│   │   ├── dependencies.py           ← Dependency injection
│   │   └── __init__.py
│   │
│   ├── 📁 models/                    ← Modelos ML
│   │   ├── credit_model.py           ← Classificador principal
│   │   └── __init__.py
│   │
│   ├── 📁 utils/                     ← Utilitários
│   │   ├── config.py                 ← Configurações via env
│   │   ├── logger.py                 ← Logging estruturado
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── 📁 notebooks/                      ← Jupyter Notebooks
│   ├── exploration.ipynb             ← EDA, treinamento, análise
│   └── __init__.py
│
├── 📁 tests/                         ← Testes automatizados
│   ├── test_api.py                   ← Testes da API
│   └── __init__.py
│
├── 📁 scripts/                       ← Scripts auxiliares
│   ├── train_model.py                ← Treinar e salvar modelo
│   ├── test_api_locally.py           ← Testes locais com requests
│   ├── test_api.sh                   ← Testes CURL (bash)
│   └── __init__.py
│
├── 📁 data/                          ← Dados (NÃO versionado)
│   ├── 📁 raw/                       ← Dados brutos
│   └── 📁 processed/                 ← Dados processados
│
├── 📁 models_trained/                ← Modelos serializados (NÃO versionado)
│   ├── credit_model.pkl              ← RandomForestClassifier
│   └── scaler.pkl                    ← StandardScaler
│
├── 📁 docker/                        ← Docker files
│   └── Dockerfile                    ← Imagem do container
│
├── 📁 logs/                          ← Logs da aplicação (NÃO versionado)
│   └── app.log
│
├── 📄 docker-compose.yml             ← Orquestração Docker
├── 📄 Makefile                       ← Automação de tasks
├── 📄 requirements.txt               ← Dependências Python
├── 📄 pytest.ini                     ← Configuração dos testes
├── 📄 .coveragerc                    ← Configuração code coverage
├── 📄 pyproject.toml                 ← Configuração de ferramentas
├── 📄 .env.example                   ← Exemplo de variáveis de env
├── 📄 .gitignore                     ← Git ignore
├── 📄 .github/                       ← GitHub workflows (opcional)
├── 📄 README.md                      ← Documentação principal
├── 📄 CHECKLIST.md                   ← Checklist de desenvolvimento
└── 📄 PROJECT_STRUCTURE.md           ← Este arquivo
```

## 📌 Descrição dos Principais Diretórios

### `src/`
Código-fonte principal da aplicação, estruturado em:
- **api/**: FastAPI app, rotas, schemas de validação
- **models/**: Lógica ML (treino, predição, serialização)
- **utils/**: Config, logging, e funções auxiliares

### `notebooks/`
Jupyter Notebooks para:
- Exploração de dados (EDA)
- Validação de hipóteses
- Visualizações e análise
- Treinamento no ambiente exploratório

### `tests/`
Testes automatizados:
- Testes unitários
- Testes de integração
- Testes da API (TestClient)
- Coverage >80%

### `scripts/`
Scripts auxiliares:
- `train_model.py`: Treinar e serializar modelo
- `test_api_locally.py`: Testes com requests library
- `test_api.sh`: Testes com CURL

### `docker/`
Containerização:
- Dockerfile com Python 3.11-slim
- Health checks configurados
- Variáveis de ambiente

### `data/` e `models_trained/`
Ignorados no Git (.gitignore):
- Dados brutos/processados
- Modelos treinados em pickle
- Logs da aplicação

## 🚀 Quick Start

```bash
# 1. Instalar
make install

# 2. Treinar modelo
make train-model

# 3. Rodar API
make run

# 4. Testar
make test

# 5. Docker
make docker-run
```

---
**Desenvolvido com padrões profissionais de ML + Software Engineering**
