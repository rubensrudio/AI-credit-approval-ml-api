# 📋 Checklist Detalhado - Credit Approval ML API

## 🚀 Fase 1: Setup Inicial (30 min)

- [ ] **Clonar/Iniciar Repositório**
  - [ ] `git clone` ou criar novo repo
  - [ ] `git init` e primeiro commit

- [ ] **Ambiente Python**
  - [ ] Criar venv: `python -m venv venv`
  - [ ] Ativar: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux)
  - [ ] Instalar dependências: `make install`

- [ ] **Arquitetura de Pastas**
  - [ ] Validar estrutura: `src/`, `tests/`, `notebooks/`, `data/`, `scripts/`, `docker/`
  - [ ] Criar `.env` a partir de `.env.example`

- [ ] **Validação Inicial**
  - [ ] Verificar `python --version` >= 3.11
  - [ ] Verificar imports: `python -c "import fastapi; print('OK')"`


## 📊 Fase 2: Exploração e Modelagem (2-3h)

- [ ] **EDA (Exploratory Data Analysis)**
  - [ ] Abrir `notebooks/exploration.ipynb`
  - [ ] Gerar dados sintéticos
  - [ ] Análise estatística (mean, std, quantiles)
  - [ ] Visualizações (histogramas, boxplots)
  - [ ] Correlação entre features
  - [ ] Verificar imbalance de classes

- [ ] **Feature Engineering**
  - [ ] Normalização/Scaling (StandardScaler) ✓
  - [ ] Tratamento de outliers (se necessário)
  - [ ] Feature selection (se necessário)
  - [ ] Documentar transformações

- [ ] **Treinamento do Modelo**
  - [ ] Executar `make train-model`
  - [ ] Validar: `models_trained/credit_model.pkl` criado
  - [ ] Validar: `models_trained/scaler.pkl` criado
  - [ ] Verificar métricas (acurácia, AUC)
  - [ ] Teste em dados novos
  - [ ] Feature importance analysis

- [ ] **Validação do Modelo**
  - [ ] Treino vs Teste accuracy
  - [ ] Confusion Matrix
  - [ ] ROC-AUC curve
  - [ ] Classification Report
  - [ ] Cross-validation (opcional)


## 🔌 Fase 3: API REST (2-3h)

- [ ] **Schemas Pydantic**
  - [ ] `PredictionRequest` com validação
  - [ ] `PredictionResponse` com tipos corretos
  - [ ] `HealthResponse` para status
  - [ ] Field descriptions (documentation)

- [ ] **Carregamento do Modelo**
  - [ ] `get_model()` dependency function
  - [ ] Lazy loading (primeira requisição)
  - [ ] Cache de instância
  - [ ] Error handling (modelo não encontrado)

- [ ] **Rotas/Endpoints**
  - [ ] `GET /api/v1/health` ✓
  - [ ] `POST /api/v1/predict` ✓
  - [ ] Type hints em todas as funções
  - [ ] Docstrings em português
  - [ ] Error responses (400, 422, 500)

- [ ] **Configuração da App**
  - [ ] FastAPI app factory
  - [ ] CORS middleware
  - [ ] Logging no startup/shutdown
  - [ ] Título, versão, descrição
  - [ ] Rotas organizadas em módulos

- [ ] **Testing Manual**
  - [ ] Testar /health em http://localhost:8000/api/v1/health
  - [ ] Testar /predict com curl ou Postman
  - [ ] Validar response schema
  - [ ] Testar validação (dados inválidos)
  - [ ] Acessar Swagger docs: http://localhost:8000/docs


## ✅ Fase 4: Testes Automatizados (1-2h)

- [ ] **Setup Pytest**
  - [ ] `pytest.ini` ou config em `pyproject.toml`
  - [ ] Fixtures criadas
  - [ ] TestClient configurado

- [ ] **Testes da API**
  - [ ] Test health check endpoint
  - [ ] Test successful prediction
  - [ ] Test input validation
  - [ ] Test missing fields
  - [ ] Test edge cases

- [ ] **Cobertura de Testes**
  - [ ] Executar: `make test-cov`
  - [ ] Target: > 80% cobertura
  - [ ] Gerar relatório HTML
  - [ ] Identificar code gaps

- [ ] **Validação de Testes**
  - [ ] Todos testes passando
  - [ ] `make test` sem erros
  - [ ] `pytest -v` com output claro


## 🐳 Fase 5: Docker e Containerização (1-2h)

- [ ] **Dockerfile**
  - [ ] Base image: `python:3.11-slim`
  - [ ] WORKDIR definido
  - [ ] Requirements copiados e instalados
  - [ ] Código copiado
  - [ ] EXPOSE 8000
  - [ ] Healthcheck configurado
  - [ ] CMD uvicorn correto

- [ ] **docker-compose.yml**
  - [ ] Service `credit-api` definido
  - [ ] Build context correto
  - [ ] Ports mapeadas
  - [ ] Environment vars configuradas
  - [ ] Volumes para models e logs
  - [ ] Health check

- [ ] **Build e Teste**
  - [ ] Executar: `make docker-build`
  - [ ] Validar: `docker images | grep credit`
  - [ ] Executar: `make docker-run`
  - [ ] Testar: `curl http://localhost:8000/api/v1/health`
  - [ ] Logs: `docker logs credit-api`
  - [ ] Stop: `make docker-stop`

- [ ] **Troubleshooting**
  - [ ] Verificar volumes estão mounted
  - [ ] Model path acessível no container
  - [ ] Porta 8000 não em conflito
  - [ ] Permissions corretos


## 🎨 Fase 6: Padrões de Código e Qualidade (1h)

- [ ] **Type Hints**
  - [ ] Verificar todo arquivo `.py`
  - [ ] Funções com input/output tipos
  - [ ] Classes com type annotations
  - [ ] `mypy` passar (opcional)

- [ ] **Logging**
  - [ ] Usar `get_logger(__name__)` em todos módulos
  - [ ] Logs estruturados (JSON)
  - [ ] Log levels apropriados (INFO, ERROR, WARNING)
  - [ ] `logs/` directory funcional

- [ ] **Configurações**
  - [ ] Todas env vars em `.env.example`
  - [ ] `Settings` classe usada
  - [ ] Senhas/secrets em `.env` (nunca committed)
  - [ ] Modo production vs development

- [ ] **Docstrings e Comentários**
  - [ ] Funções com docstrings
  - [ ] Português claro
  - [ ] Args e Returns documentados
  - [ ] Classes com __doc__

- [ ] **Formatação de Código** (opcional)
  - [ ] Executar: `make format`
  - [ ] Black config (line length 100)
  - [ ] isort para imports
  - [ ] flake8 ou pylint: `make lint`


## 📚 Fase 7: Documentação (1h)

- [ ] **README.md**
  - [ ] Visão geral do projeto ✓
  - [ ] Arquitetura explicada ✓
  - [ ] Setup instructions ✓
  - [ ] Como treinar modelo ✓
  - [ ] Como rodar API ✓
  - [ ] Docker instructions ✓
  - [ ] API endpoints documentados ✓
  - [ ] Exemplos de curl/requests ✓

- [ ] **Documentação Inline**
  - [ ] Docstrings em todas funções
  - [ ] Type hints documentados
  - [ ] Config vars explicadas
  - [ ] Comments para lógica complexa

- [ ] **OpenAPI/Swagger**
  - [ ] Automático via FastAPI ✓
  - [ ] Acessível em /docs
  - [ ] Descriptions nas rotas
  - [ ] Exemplos nos schemas

- [ ] **Notebook**
  - [ ] Código bem organizado
  - [ ] Markdown explanations ✓
  - [ ] Visualizações funcionando
  - [ ] Reprodutível passo a passo


## 🚀 Fase 8: Deploy Preparação (Opcional)

- [ ] **Production Readiness**
  - [ ] Environment variables corretos
  - [ ] Logging em arquivos
  - [ ] Error handling robusto
  - [ ] Health checks funcionando
  - [ ] Secrets em .env

- [ ] **CI/CD (GitHub Actions)**
  - [ ] `.github/workflows/test.yml` (rodar testes)
  - [ ] `.github/workflows/docker.yml` (build image)
  - [ ] Validação de mudanças

- [ ] **Platforms (opcional)**
  - [ ] Heroku: Procfile + runtime.txt
  - [ ] Railway: railway.json
  - [ ] AWS: Lambda / Fargate
  - [ ] GCP / Azure

- [ ] **Security**
  - [ ] HTTPS em produção
  - [ ] API keys se necessário
  - [ ] CORS configurado corretamente
  - [ ] Input validation
  - [ ] No secrets em código


## ✨ Fase 9: Verificação Final

- [ ] **Funcionalidade End-to-End**
  - [ ] `make install` sem erros
  - [ ] `make train-model` + modelo criado
  - [ ] `make run` + API funciona
  - [ ] `make test` tudo passa
  - [ ] `make docker-run` funciona

- [ ] **Documentação Completa**
  - [ ] README cobrindo tudo
  - [ ] Código bem documentado
  - [ ] Exemplos funcionam
  - [ ] Instrções claras

- [ ] **Git/Repository**
  - [ ] `.gitignore` correto
  - [ ] Sem arquivos temporários versionados
  - [ ] README no root
  - [ ] Commits descritivos
  - [ ] LICENSE presente

- [ ] **Portfolio Quality**
  - [ ] Código profissional
  - [ ] Padrões OOP/FP
  - [ ] PEP 8 compliance
  - [ ] Tests inclusos
  - [ ] Docker incluído
  - [ ] GitHub README impressionante


---

## 📊 Progresso

| Fase | Status | ETA |
|------|--------|-----|
| 1. Setup | ✓ | 30min |
| 2. Modelagem | ⏳ | 2-3h |
| 3. API | ⏳ | 2-3h |
| 4. Testes | ⏳ | 1-2h |
| 5. Docker | ⏳ | 1-2h |
| 6. Qualidade | ⏳ | 1h |
| 7. Docs | ⏳ | 1h |
| 8. Deploy | ⏳ | 1h (opt) |
| 9. Final Check | ⏳ | 30min |
| **TOTAL** | | **10-15h** |

---

## 🎯 Success Criteria

- [ ] Todas as fases marcadas como ✓
- [ ] `make test` passa com sucesso
- [ ] `make docker-run` funciona
- [ ] API responde em http://localhost:8000/docs
- [ ] Modelo prediz corretamente
- [ ] Código é legível e profissional
- [ ] README é claro e completo
- [ ] Pronto para portfólio!

---

**Ao terminar toda checklist: PRONTO PARA PRODUÇÃO! 🚀**
