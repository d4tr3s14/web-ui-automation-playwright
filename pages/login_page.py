"""Página de inicio de sesión de SauceDemo."""
from __future__ import annotations

from .base_page import BasePage


class LoginPage(BasePage):
    path = "/"

    # Locators
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR = '[data-test="error"]'

    def load(self) -> "LoginPage":
        self.navigate()
        return self

    def login(self, username: str, password: str) -> None:
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def error_message(self) -> str:
        return self.text(self.ERROR)

    def has_error(self) -> bool:
        return self.is_visible(self.ERROR)
