"""Páginas del flujo de checkout de SauceDemo (información, resumen y confirmación)."""
from __future__ import annotations

from .base_page import BasePage


class CheckoutPage(BasePage):
    path = "/checkout-step-one.html"

    # Paso 1: información del comprador
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = '[data-test="continue"]'

    # Paso 2: resumen
    FINISH = '[data-test="finish"]'

    # Confirmación
    COMPLETE_HEADER = ".complete-header"

    def fill_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.POSTAL_CODE, postal_code)

    def continue_to_summary(self) -> None:
        self.click(self.CONTINUE)

    def finish(self) -> None:
        self.click(self.FINISH)

    def success_message(self) -> str:
        return self.text(self.COMPLETE_HEADER)

    def is_complete(self) -> bool:
        return self.is_visible(self.COMPLETE_HEADER)
