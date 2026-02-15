"""
Script to train the credit model.
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
    Generate synthetic credit data for demonstration.

    Returns:
        X: Features (DataFrame)
        y: Target (Series)
    """
    logger.info(f"Generating {n_samples} synthetic samples...")

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

    # Target: simple rule for synthetic data
    # Credit approved if: (score > 600) AND (income > loan_amount * 0.2) AND (age > 21)
    y = (
        (X["credit_score"] > 600)
        & (X["income"] > X["loan_amount"] * 0.2)
        & (X["age"] > 21)
    ).astype(int)

    logger.info(f"✓ Data generated: {len(X)} samples")
    logger.info(f"  Distribution: {(y == 1).sum()} approved, {(y == 0).sum()} rejected")

    return X, y


def main() -> None:
    """Main training function."""
    logger.info("=" * 60)
    logger.info("CREDIT APPROVAL MODEL TRAINING")
    logger.info("=" * 60)

    # Generate data
    X, y = generate_synthetic_data(n_samples=1000)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    logger.info(f"✓ Data split: {len(X_train)} train, {len(X_test)} test")

    # Train model
    model = CreditApprovalModel()
    metrics = model.train(X_train, y_train)

    logger.info(f"✓ Training completed:")
    logger.info(f"  Train accuracy: {metrics['train_accuracy']:.4f}")
    logger.info(f"  Features: {metrics['n_features']}")
    logger.info(f"  Estimators: {metrics['n_estimators']}")

    # Evaluate on test set
    predictions = model.predict(X_test)
    test_accuracy = (predictions == y_test.values).mean()
    logger.info(f"  Test accuracy: {test_accuracy:.4f}")

    # Save model
    model_dir = Path("models_trained")
    model_dir.mkdir(exist_ok=True)

    model.save(
        str(model_dir / "credit_model.pkl"),
        str(model_dir / "scaler.pkl"),
    )

    logger.info("=" * 60)
    logger.info("✓ MODEL TRAINED AND SAVED SUCCESSFULLY!")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
