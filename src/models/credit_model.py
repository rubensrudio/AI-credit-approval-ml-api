"""
Machine Learning models module.
"""
import pickle
from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

from src.utils.logger import get_logger

logger = get_logger(__name__)


class CreditApprovalModel:
    """Credit approval classification model."""

    def __init__(self) -> None:
        self.model: RandomForestClassifier | None = None
        self.scaler: StandardScaler | None = None
        self.feature_names: list[str] | None = None

    def train(
        self,
        X_train: pd.DataFrame,
        y_train: pd.Series,
    ) -> dict:
        """
        Train the classification model.

        Args:
            X_train: Training features
            y_train: Training target

        Returns:
            Training metrics
        """
        logger.info("Starting model training...")

        # Normalize features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X_train)

        # Train model
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1,
        )
        self.model.fit(X_scaled, y_train)

        # Store feature names
        self.feature_names = X_train.columns.tolist()

        # Calculate training accuracy
        train_score = self.model.score(X_scaled, y_train)

        logger.info(f"Model trained successfully. Accuracy: {train_score:.4f}")

        return {
            "train_accuracy": float(train_score),
            "n_features": len(self.feature_names),
            "n_estimators": self.model.n_estimators,
        }

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Perform prediction.

        Args:
            X: Features for prediction

        Returns:
            Predictions (0 = Rejected, 1 = Approved)
        """
        if self.model is None or self.scaler is None:
            raise ValueError("Model not trained. Run train() first.")

        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Return prediction probabilities.

        Args:
            X: Features for prediction

        Returns:
            Probabilities [prob_rejected, prob_approved]
        """
        if self.model is None or self.scaler is None:
            raise ValueError("Model not trained. Run train() first.")

        X_scaled = self.scaler.transform(X)
        return self.model.predict_proba(X_scaled)

    def save(self, model_path: str, scaler_path: str) -> None:
        """
        Save model and scaler to pickle files.

        Args:
            model_path: Path to model file
            scaler_path: Path to scaler file
        """
        if self.model is None or self.scaler is None:
            raise ValueError("Model not trained.")

        Path(model_path).parent.mkdir(parents=True, exist_ok=True)

        with open(model_path, "wb") as f:
            pickle.dump(self.model, f)

        with open(scaler_path, "wb") as f:
            pickle.dump(self.scaler, f)

        logger.info(f"Model saved at {model_path}")
        logger.info(f"Scaler saved at {scaler_path}")

    def load(self, model_path: str, scaler_path: str) -> None:
        """
        Load model and scaler from pickle files.

        Args:
            model_path: Path to model file
            scaler_path: Path to scaler file
        """
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        with open(scaler_path, "rb") as f:
            self.scaler = pickle.load(f)

        logger.info(f"Model loaded from {model_path}")
