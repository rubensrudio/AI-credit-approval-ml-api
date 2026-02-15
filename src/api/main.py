"""
Aplicação FastAPI principal.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import router
from src.utils.config import get_settings
from src.utils.logger import get_logger, setup_logging

logger = get_logger(__name__)


def create_app() -> FastAPI:
    """Factory para criar e configurar aplicação FastAPI."""
    setup_logging()
    settings = get_settings()

    app = FastAPI(
        title=settings.api_title,
        version=settings.api_version,
        description="API de classificação para aprovação de crédito com Machine Learning",
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Rotas
    app.include_router(router)

    @app.on_event("startup")
    async def startup() -> None:
        logger.info(f"Iniciando {settings.api_title} v{settings.api_version}")
        logger.info(f"Ambiente: {settings.environment}")

    @app.on_event("shutdown")
    async def shutdown() -> None:
        logger.info("Encerrando aplicação")

    return app


app = create_app()
