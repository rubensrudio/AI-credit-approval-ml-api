"""
Structured logging module.
"""
import json
import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from src.utils.config import get_settings


def setup_logging() -> None:
    """Configure structured logging with JSON format."""
    settings = get_settings()
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(settings.log_level)

    # Formato JSON
    class JsonFormatter(logging.Formatter):
        def format(self, record: logging.LogRecord) -> str:
            log_data = {
                "timestamp": self.formatTime(record),
                "level": record.levelname,
                "message": record.getMessage(),
                "module": record.module,
                "function": record.funcName,
                "line": record.lineno,
            }
            if record.exc_info:
                log_data["exception"] = self.formatException(record.exc_info)
            return json.dumps(log_data, ensure_ascii=False)

    # Handler para arquivo
    file_handler = RotatingFileHandler(
        log_dir / "app.log", maxBytes=10_000_000, backupCount=5
    )
    file_handler.setFormatter(JsonFormatter())
    logger.addHandler(file_handler)

    # Handler para console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(console_handler)


def get_logger(name: str) -> logging.Logger:
    """Get logger with specific name."""
    return logging.getLogger(name)
