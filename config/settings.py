"""
Configuración del framework (sobreescribible por variables de entorno).

Las credenciales de SauceDemo son **públicas y de demostración** (las publica el
propio sitio), por lo que no constituyen un secreto.
"""
from __future__ import annotations

import os


def _bool(name: str, default: bool) -> bool:
    val = os.getenv(name)
    if val is None:
        return default
    return val.strip().lower() in ("1", "true", "yes", "y", "on")


# Sitio bajo prueba
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")

# Credenciales de demo (públicas)
STANDARD_USER = os.getenv("SAUCE_USER", "standard_user")
LOCKED_USER = os.getenv("SAUCE_LOCKED_USER", "locked_out_user")
PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")

# Ejecución del navegador
HEADLESS = _bool("HEADLESS", True)
BROWSER = os.getenv("BROWSER", "chromium")          # chromium | firefox | webkit
SLOW_MO = int(os.getenv("SLOW_MO", "0"))            # ms entre acciones (debug)
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))  # ms
VIEWPORT = {"width": 1366, "height": 768}

# Artefactos de evidencia
ARTIFACTS_DIR = os.getenv("ARTIFACTS_DIR", "test-results")
