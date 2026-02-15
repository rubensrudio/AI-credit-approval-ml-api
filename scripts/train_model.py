"""
Script para treinar o modelo de crédito.
"""
import logging
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.models.credit_model import CreditApprovalModel

# Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_synthetic_data(n_samples: int = 1000) -> tuple[pd.DataFrame, pd.Series]:
    """
    Gera dados sintéticos de crédito para demonstração.

    Returns:
        X: Features (DataFrame)
        y: Target (Series)
    """
    logger.info(f"Gerando {n_samples} amostras sintéticas...")

    np.random.seed(42)

    X = pd.DataFrame(
        {
            "age": np.random.randint(18, 75, n_samples),
            "income": np.random.randint(20000, 200000, n_samples),
            "credit_score": np.random.randint(300, 850, n_samples),
            "loan_amount": np.random.randint(5000, 100000, n_samples),
            "employment_years": np.random.randint(0, 50, n_samples),
            "existing_debts": np.random.randint(0, 50000, n_samples),
        }
    )

    # Target: regra simples para dados sintéticos
    # Crédito aprovado se: (score > 600) E (income > loan_amount * 0.2) E (idade > 21)
    y = (
        (X["credit_score"] > 600)
        & (X["income"] > X["loan_amount"] * 0.2)
        & (X["age"] > 21)
    ).astype(int)

    logger.info(f"✓ Dados gerados: {len(X)} amostras")
    logger.info(f"  Distribuição: {(y == 1).sum()} aprovados, {(y == 0).sum()} reprovados")

    return X, y


def main() -> None:
    """Função principal de treinamento."""
    logger.info("=" * 60)
    logger.info("TREINAMENTO DO MODELO DE APROVAÇÃO DE CRÉDITO")
    logger.info("=" * 60)

    # Gerar dados
    X, y = generate_synthetic_data(n_samples=1000)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    logger.info(f"✓ Dados divididos: {len(X_train)} treino, {len(X_test)} teste")

    # Treinar modelo
    model = CreditApprovalModel()
    metrics = model.train(X_train, y_train)

    logger.info(f"✓ Treinamento concluído:")
    logger.info(f"  Acurácia treino: {metrics['train_accuracy']:.4f}")
    logger.info(f"  Features: {metrics['n_features']}")
    logger.info(f"  Estimators: {metrics['n_estimators']}")

    # Avaliar no teste
    predictions = model.predict(X_test)
    test_accuracy = (predictions == y_test.values).mean()
    logger.info(f"  Acurácia teste: {test_accuracy:.4f}")

    # Salvar modelo
    model_dir = Path("models_trained")
    model_dir.mkdir(exist_ok=True)

    model.save(
        str(model_dir / "credit_model.pkl"),
        str(model_dir / "scaler.pkl"),
    )

    logger.info("=" * 60)
    logger.info("✓ MODELO TREINADO E SALVO COM SUCESSO!")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
