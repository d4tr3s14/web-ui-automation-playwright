"""Página del carrito de compras de SauceDemo."""
from __future__ import annotations

from .base_page import BasePage


class CartPage(BasePage):
    path = "/cart.html"

    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    CHECKOUT = '[data-test="checkout"]'
    CONTINUE_SHOPPING = '[data-test="continue-shopping"]'

    def item_names(self) -> list[str]:
        return [t.strip() for t in self.page.locator(self.ITEM_NAME).all_text_contents()]

    def item_count(self) -> int:
        return self.count(self.CART_ITEM)

    def checkout(self) -> None:
        self.click(self.CHECKOUT)
