"""Página de inventario/productos de SauceDemo."""
from __future__ import annotations

from .base_page import BasePage


class InventoryPage(BasePage):
    path = "/inventory.html"

    TITLE = ".title"
    ITEM = ".inventory_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT = ".product_sort_container"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT = "#logout_sidebar_link"

    def is_loaded(self) -> bool:
        return self.is_visible(self.TITLE) and self.text(self.TITLE) == "Products"

    def product_count(self) -> int:
        return self.count(self.ITEM)

    def prices(self) -> list[float]:
        raw = self.page.locator(self.ITEM_PRICE).all_text_contents()
        return [float(p.strip().lstrip("$")) for p in raw]

    def logout(self) -> None:
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT)

    def add_item_to_cart(self, name: str) -> None:
        item = self.page.locator(self.ITEM).filter(has_text=name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_item_from_cart(self, name: str) -> None:
        item = self.page.locator(self.ITEM).filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def cart_count(self) -> int:
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.text(self.CART_BADGE))

    def product_names(self) -> list[str]:
        return [t.strip() for t in self.page.locator(self.ITEM_NAME).all_text_contents()]

    def sort_by(self, value: str) -> None:
        # value: az | za | lohi | hilo
        self.page.select_option(self.SORT, value)

    def open_cart(self) -> None:
        self.click(self.CART_LINK)
