"""
Dependências da API.
"""
from pathlib import Path

import pandas as pd

from src.models.credit_model import CreditApprovalModel
from src.utils.config import get_settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Instância global do modelo
_model_instance: CreditApprovalModel | None = None


def get_model() -> CreditApprovalModel:
    """Retorna instância do modelo (lazy loading)."""
    global _model_instance

    if _model_instance is None:
        logger.info("Carregando modelo de crédito...")
        _model_instance = CreditApprovalModel()

        settings = get_settings()
        model_path = Path(settings.model_path)
        scaler_path = Path(settings.scaler_path)

        if not model_path.exists() or not scaler_path.exists():
            logger.warning(
                f"Modelo não encontrado em {model_path}. "
                "Certifique-se de treinar o modelo primeiro."
            )
            raise FileNotFoundError(f"Modelo não encontrado em {model_path}")

        _model_instance.load(str(model_path), str(scaler_path))
        logger.info("Modelo carregado com sucesso")

    return _model_instance


def model_loaded() -> bool:
    """Verifica se modelo está carregado."""
    return _model_instance is not None
