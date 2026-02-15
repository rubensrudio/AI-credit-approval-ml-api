"""
Módulo de modelos ML.
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
    """Modelo de classificação para aprovação de crédito."""

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
        Treina o modelo de classificação.

        Args:
            X_train: Features de treino
            y_train: Target de treino

        Returns:
            Métricas de treino
        """
        logger.info("Iniciando treinamento do modelo...")

        # Normalizar features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X_train)

        # Treinar modelo
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1,
        )
        self.model.fit(X_scaled, y_train)

        # Armazenar nomes de features
        self.feature_names = X_train.columns.tolist()

        # Calcular acurácia de treino
        train_score = self.model.score(X_scaled, y_train)

        logger.info(f"Modelo treinado com sucesso. Acurácia: {train_score:.4f}")

        return {
            "train_accuracy": float(train_score),
            "n_features": len(self.feature_names),
            "n_estimators": self.model.n_estimators,
        }

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Realiza predição.

        Args:
            X: Features para predição

        Returns:
            Predições (0 = Reprovado, 1 = Aprovado)
        """
        if self.model is None or self.scaler is None:
            raise ValueError("Modelo não foi treinado. Execute train() primeiro.")

        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Retorna probabilidades das predições.

        Args:
            X: Features para predição

        Returns:
            Probabilidades [prob_reprovado, prob_aprovado]
        """
        if self.model is None or self.scaler is None:
            raise ValueError("Modelo não foi treinado. Execute train() primeiro.")

        X_scaled = self.scaler.transform(X)
        return self.model.predict_proba(X_scaled)

    def save(self, model_path: str, scaler_path: str) -> None:
        """
        Salva modelo e scaler em arquivos pickle.

        Args:
            model_path: Caminho do arquivo do modelo
            scaler_path: Caminho do arquivo do scaler
        """
        if self.model is None or self.scaler is None:
            raise ValueError("Modelo não foi treinado.")

        Path(model_path).parent.mkdir(parents=True, exist_ok=True)

        with open(model_path, "wb") as f:
            pickle.dump(self.model, f)

        with open(scaler_path, "wb") as f:
            pickle.dump(self.scaler, f)

        logger.info(f"Modelo salvo em {model_path}")
        logger.info(f"Scaler salvo em {scaler_path}")

    def load(self, model_path: str, scaler_path: str) -> None:
        """
        Carrega modelo e scaler de arquivos pickle.

        Args:
            model_path: Caminho do arquivo do modelo
            scaler_path: Caminho do arquivo do scaler
        """
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        with open(scaler_path, "rb") as f:
            self.scaler = pickle.load(f)

        logger.info(f"Modelo carregado de {model_path}")
