"""
Página base del Page Object Model.

Encapsula la `Page` de Playwright y expone acciones de alto nivel y robustas
(con esperas automáticas) para que las páginas hijas no repitan código ni
manejen `locators` crudos en las pruebas.
"""
from __future__ import annotations

from playwright.sync_api import Page, expect

from config import settings


class BasePage:
    """Clase base de todas las páginas."""

    # Cada página hija define su ruta relativa (si aplica).
    path: str = ""

    def __init__(self, page: Page):
        self.page = page

    # ------------------------------------------------------------------ #
    # Navegación
    # ------------------------------------------------------------------ #
    def navigate(self, path: str | None = None) -> None:
        url = settings.BASE_URL + (path if path is not None else self.path)
        self.page.goto(url, wait_until="domcontentloaded")

    @property
    def current_url(self) -> str:
        return self.page.url

    def title(self) -> str:
        return self.page.title()

    # ------------------------------------------------------------------ #
    # Acciones (con auto-espera de Playwright)
    # ------------------------------------------------------------------ #
    def click(self, selector: str) -> None:
        self.page.click(selector)

    def fill(self, selector: str, value: str) -> None:
        self.page.fill(selector, value)

    def text(self, selector: str) -> str:
        return (self.page.text_content(selector) or "").strip()

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def count(self, selector: str) -> int:
        return self.page.locator(selector).count()

    # ------------------------------------------------------------------ #
    # Aserciones expresivas (web-first assertions de Playwright)
    # ------------------------------------------------------------------ #
    def expect_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()

    def expect_url_contains(self, fragment: str):
        expect(self.page).to_have_url(lambda url: fragment in url)
