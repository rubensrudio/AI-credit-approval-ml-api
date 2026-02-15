"""
Main API routes.
"""
from typing import Annotated

import pandas as pd
from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_model, model_loaded
from src.api.schemas import PredictionRequest, PredictionResponse, HealthResponse
from src.models.credit_model import CreditApprovalModel
from src.utils.config import get_settings
from src.utils.logger import get_logger

router = APIRouter(prefix="/api/v1", tags=["Credit Approval"])
logger = get_logger(__name__)


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Application status and model availability."""
    settings = get_settings()
    return HealthResponse(
        status="healthy",
        version=settings.api_version,
        model_loaded=model_loaded(),
    )


@router.post("/predict", response_model=PredictionResponse)
async def predict(
    request: PredictionRequest,
    model: Annotated[CreditApprovalModel, Depends(get_model)],
) -> PredictionResponse:
    """
    Predict credit approval.

    Receives customer data and returns whether credit should be approved.
    """
    try:
        # Prepare data for prediction
        X = pd.DataFrame(
            {
                "age": [request.age],
                "income": [request.income],
                "credit_score": [request.credit_score],
                "loan_amount": [request.loan_amount],
                "employment_years": [request.employment_years],
                "existing_debts": [request.existing_debts],
            }
        )

        # Prediction
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0][1]

        # Determine risk level
        if probability >= 0.8:
            risk_level = "low"
        elif probability >= 0.5:
            risk_level = "medium"
        else:
            risk_level = "high"

        logger.info(
            f"Prediction made: approved={bool(prediction)}, "
            f"probability={probability:.4f}"
        )

        return PredictionResponse(
            approved=bool(prediction),
            approval_probability=round(float(probability), 4),
            risk_level=risk_level,
        )

    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing prediction") from e
