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

    # Validación
    ERROR = '[data-test="error"]'

    # Paso 2: resumen del pedido
    FINISH = '[data-test="finish"]'
    SUBTOTAL = ".summary_subtotal_label"   # "Item total: $29.99"
    TAX = ".summary_tax_label"             # "Tax: $2.40"
    TOTAL = ".summary_total_label"         # "Total: $32.39"

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

    def error_message(self) -> str:
        return self.text(self.ERROR)

    def _money(self, selector: str) -> float:
        # Extrae el importe de textos como "Item total: $29.99".
        raw = self.text(selector)
        return float(raw.split("$")[1].strip())

    def item_total(self) -> float:
        return self._money(self.SUBTOTAL)

    def tax(self) -> float:
        return self._money(self.TAX)

    def total(self) -> float:
        return self._money(self.TOTAL)

    def success_message(self) -> str:
        return self.text(self.COMPLETE_HEADER)

    def is_complete(self) -> bool:
        return self.is_visible(self.COMPLETE_HEADER)
