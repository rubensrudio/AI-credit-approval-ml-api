"""
API dependencies.
"""
from pathlib import Path

import pandas as pd

from src.models.credit_model import CreditApprovalModel
from src.utils.config import get_settings
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Global model instance
_model_instance: CreditApprovalModel | None = None


def get_model() -> CreditApprovalModel:
    """Return model instance (lazy loading)."""
    global _model_instance

    if _model_instance is None:
        logger.info("Loading credit model...")
        _model_instance = CreditApprovalModel()

        settings = get_settings()
        model_path = Path(settings.model_path)
        scaler_path = Path(settings.scaler_path)

        if not model_path.exists() or not scaler_path.exists():
            logger.warning(
                f"Model not found at {model_path}. "
                "Make sure to train the model first."
            )
            raise FileNotFoundError(f"Model not found at {model_path}")

        _model_instance.load(str(model_path), str(scaler_path))
        logger.info("Model loaded successfully")

    return _model_instance


def model_loaded() -> bool:
    """Check if model is loaded."""
    return _model_instance is not None
