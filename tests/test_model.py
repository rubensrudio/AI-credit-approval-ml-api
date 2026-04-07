"""
Tests for CreditApprovalModel.
"""
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

import numpy as np
import pandas as pd
import pytest

from src.models.credit_model import CreditApprovalModel


@pytest.fixture
def sample_data() -> tuple[pd.DataFrame, pd.Series]:
    """Generate sample data for training."""
    np.random.seed(42)
    n = 100
    X = pd.DataFrame({
        "age": np.random.randint(18, 75, n),
        "income": np.random.randint(20000, 200000, n),
        "credit_score": np.random.randint(300, 850, n),
        "loan_amount": np.random.randint(5000, 100000, n),
        "employment_years": np.random.randint(0, 50, n),
        "existing_debts": np.random.randint(0, 50000, n),
    })
    y = ((X["credit_score"] > 600) & (X["income"] > X["loan_amount"] * 0.2)).astype(int)
    return X, y


@pytest.fixture
def trained_model(sample_data) -> CreditApprovalModel:
    """Train a model for testing."""
    X, y = sample_data
    model = CreditApprovalModel()
    model.train(X, y)
    return model


class TestTrain:
    """Tests for model training."""

    def test_train_returns_metrics(self, trained_model: CreditApprovalModel) -> None:
        metrics = trained_model.train(*generate_sample(50))
        assert "train_accuracy" in metrics
        assert "n_features" in metrics
        assert "n_estimators" in metrics
        assert 0.0 <= metrics["train_accuracy"] <= 1.0

    def test_train_sets_scaler(self, trained_model: CreditApprovalModel) -> None:
        assert trained_model.scaler is not None

    def test_train_sets_feature_names(self, trained_model: CreditApprovalModel) -> None:
        assert trained_model.feature_names == [
            "age", "income", "credit_score", "loan_amount",
            "employment_years", "existing_debts",
        ]


class TestPredict:
    """Tests for prediction."""

    def test_predict_returns_array(self, trained_model: CreditApprovalModel) -> None:
        X, _ = generate_sample(5)
        result = trained_model.predict(X)
        assert isinstance(result, np.ndarray)
        assert len(result) == 5

    def test_predict_proba_returns_probabilities(self, trained_model: CreditApprovalModel) -> None:
        X, _ = generate_sample(5)
        result = trained_model.predict_proba(X)
        assert result.shape == (5, 2)
        assert np.allclose(result.sum(axis=1), 1.0)

    def test_predict_without_training_raises(self) -> None:
        model = CreditApprovalModel()
        X, _ = generate_sample(1)
        with pytest.raises(ValueError, match="not trained"):
            model.predict(X)

    def test_predict_proba_without_training_raises(self) -> None:
        model = CreditApprovalModel()
        X, _ = generate_sample(1)
        with pytest.raises(ValueError, match="not trained"):
            model.predict_proba(X)


class TestSaveLoad:
    """Tests for model serialization."""

    def test_save_and_load(self, trained_model: CreditApprovalModel, tmp_path: Path) -> None:
        model_path = str(tmp_path / "model.pkl")
        scaler_path = str(tmp_path / "scaler.pkl")

        trained_model.save(model_path, scaler_path)
        assert os.path.exists(model_path)
        assert os.path.exists(scaler_path)

        new_model = CreditApprovalModel()
        new_model.load(model_path, scaler_path)

        X, _ = generate_sample(3)
        np.testing.assert_array_equal(
            trained_model.predict(X),
            new_model.predict(X),
        )

    def test_save_untrained_raises(self) -> None:
        model = CreditApprovalModel()
        with pytest.raises(ValueError, match="not trained"):
            model.save("model.pkl", "scaler.pkl")


def generate_sample(n: int = 1) -> tuple[pd.DataFrame, pd.Series]:
    """Helper to generate sample data."""
    np.random.seed(42)
    X = pd.DataFrame({
        "age": np.random.randint(18, 75, n),
        "income": np.random.randint(20000, 200000, n),
        "credit_score": np.random.randint(300, 850, n),
        "loan_amount": np.random.randint(5000, 100000, n),
        "employment_years": np.random.randint(0, 50, n),
        "existing_debts": np.random.randint(0, 50000, n),
    })
    y = ((X["credit_score"] > 600) & (X["income"] > X["loan_amount"] * 0.2)).astype(int)
    return X, y
