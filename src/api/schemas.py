"""
Pydantic validation schemas.
"""
from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """Request schema for prediction."""

    age: float = Field(..., gt=0, le=100, description="Customer age")
    income: float = Field(..., gt=0, description="Annual income in currency")
    credit_score: float = Field(..., ge=0, le=1000, description="Credit score")
    loan_amount: float = Field(..., gt=0, description="Requested loan amount")
    employment_years: float = Field(..., ge=0, le=60, description="Years employed")
    existing_debts: float = Field(..., ge=0, description="Existing debts")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 35,
                "income": 50000,
                "credit_score": 720,
                "loan_amount": 15000,
                "employment_years": 8,
                "existing_debts": 5000,
            }
        }


class PredictionResponse(BaseModel):
    """Response schema for prediction."""

    approved: bool = Field(..., description="Credit approved or not")
    approval_probability: float = Field(..., ge=0, le=1, description="Approval probability")
    risk_level: str = Field(..., description="Risk level: low, medium, high")

    class Config:
        json_schema_extra = {
            "example": {
                "approved": True,
                "approval_probability": 0.87,
                "risk_level": "low",
            }
        }


class HealthResponse(BaseModel):
    """Response schema for health check."""

    status: str = Field(..., description="Application status")
    version: str = Field(..., description="API version")
    model_loaded: bool = Field(..., description="Model loaded in memory")
