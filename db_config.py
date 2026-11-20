"""Shared, environment-based MySQL configuration."""

from __future__ import annotations

import os
from typing import Any, Dict


DEFAULT_DATABASE = "FaceRecognitionSystem"


def get_db_config(*, include_database: bool = True) -> Dict[str, Any]:
    """Return mysql-connector settings without embedding credentials in source."""
    config: Dict[str, Any] = {
        "host": os.getenv("DB_HOST", "127.0.0.1"),
        "port": int(os.getenv("DB_PORT", "3306")),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
    }

    if include_database:
        config["database"] = os.getenv("DB_NAME", DEFAULT_DATABASE)

    auth_plugin = os.getenv("DB_AUTH_PLUGIN")
    if auth_plugin:
        config["auth_plugin"] = auth_plugin

    return config
