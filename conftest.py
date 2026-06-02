"""
Configuración de pytest + Playwright.

- Ciclo de vida del navegador/contexto/página vía fixtures.
- Captura de evidencia SOLO en fallos: screenshot + video + trace de Playwright,
  adjuntos automáticamente al reporte Allure.
- Fixtures de Page Objects listos para inyectar en los step definitions.
"""
from __future__ import annotations

import re
from pathlib import Path

import allure
import pytest
from playwright.sync_api import sync_playwright

from config import settings
from pages import CartPage, CheckoutPage, InventoryPage, LoginPage


def _slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", text)[:80]


# --------------------------------------------------------------------------- #
# Navegador (sesión) y página (por test)
# --------------------------------------------------------------------------- #
@pytest.fixture(scope="session")
def _playwright():
    pw = sync_playwright().start()
    yield pw
    pw.stop()


@pytest.fixture(scope="session")
def browser(_playwright):
    browser_type = getattr(_playwright, settings.BROWSER)
    browser = browser_type.launch(headless=settings.HEADLESS, slow_mo=settings.SLOW_MO)
    yield browser
    browser.close()


@pytest.fixture
def page(browser, request):
    artifacts = Path(settings.ARTIFACTS_DIR)
    video_dir = artifacts / "videos"
    video_dir.mkdir(parents=True, exist_ok=True)

    context = browser.new_context(viewport=settings.VIEWPORT, record_video_dir=str(video_dir))
    context.set_default_timeout(settings.DEFAULT_TIMEOUT)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    # Distingue cada ejecución por navegador en el reporte Allure.
    allure.dynamic.parameter("browser", settings.BROWSER)

    yield page

    # --- Evidencia --------------------------------------------------------- #
    rep = getattr(request.node, "rep_call", None)
    failed = rep is not None and rep.failed

    # Screenshot: solo en fallo (con la página aún abierta).
    if failed:
        try:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception:  # noqa: BLE001
            pass

    # Trace: solo en fallo (es pesado; se abre con `playwright show-trace`).
    trace_path = artifacts / f"trace-{_slug(request.node.name)}.zip"
    try:
        context.tracing.stop(path=str(trace_path) if failed else None)
    except Exception:  # noqa: BLE001
        pass

    video_path = None
    try:
        if page.video:
            video_path = page.video.path()
    except Exception:  # noqa: BLE001
        pass

    context.close()  # finaliza el archivo de video

    # Video: SIEMPRE (también cuando el test termina OK).
    if video_path and Path(video_path).exists():
        allure.attach.file(video_path, name="video", attachment_type=allure.attachment_type.WEBM)

    # Trace: adjunto solo cuando hubo fallo.
    if failed and trace_path.exists():
        allure.attach.file(str(trace_path), name="playwright-trace", extension="zip")


# --------------------------------------------------------------------------- #
# Page Objects listos para inyectar
# --------------------------------------------------------------------------- #
@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page) -> CheckoutPage:
    return CheckoutPage(page)


# --------------------------------------------------------------------------- #
# Hook: expone el resultado de cada fase a los fixtures (para detectar fallos)
# --------------------------------------------------------------------------- #
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# --------------------------------------------------------------------------- #
# Metadatos del entorno para Allure
# --------------------------------------------------------------------------- #
@pytest.fixture(scope="session", autouse=True)
def _allure_environment():
    results = Path("allure-results")
    results.mkdir(parents=True, exist_ok=True)
    (results / "environment.properties").write_text(
        f"Base.URL={settings.BASE_URL}\n"
        f"Browser={settings.BROWSER}\n"
        f"Headless={settings.HEADLESS}\n",
        encoding="utf-8",
    )
    yield
