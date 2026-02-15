"""
Schemas de validação Pydantic.
"""
from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    """Schema para requisição de predição."""

    age: float = Field(..., gt=0, le=100, description="Idade do cliente")
    income: float = Field(..., gt=0, description="Renda anual em reais")
    credit_score: float = Field(..., ge=0, le=1000, description="Score de crédito")
    loan_amount: float = Field(..., gt=0, description="Valor do empréstimo solicitado")
    employment_years: float = Field(..., ge=0, le=60, description="Anos de emprego")
    existing_debts: float = Field(..., ge=0, description="Débitos existentes")

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
    """Schema para resposta de predição."""

    approved: bool = Field(..., description="Crédito aprovado ou não")
    approval_probability: float = Field(..., ge=0, le=1, description="Probabilidade de aprovação")
    risk_level: str = Field(..., description="Nível de risco: low, medium, high")

    class Config:
        json_schema_extra = {
            "example": {
                "approved": True,
                "approval_probability": 0.87,
                "risk_level": "low",
            }
        }


class HealthResponse(BaseModel):
    """Schema para resposta de health check."""

    status: str = Field(..., description="Status da aplicação")
    version: str = Field(..., description="Versão da API")
    model_loaded: bool = Field(..., description="Modelo carregado na memória")
