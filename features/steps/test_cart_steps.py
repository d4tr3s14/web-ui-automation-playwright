"""Steps del feature de carrito (usa los pasos compartidos de conftest)."""
from __future__ import annotations

from pytest_bdd import parsers, scenarios, then

scenarios("cart.feature")


@then(parsers.parse("el contador del carrito muestra {n:d}"))
def cart_badge_shows(inventory_page, n):
    assert inventory_page.cart_count() == n


@then(parsers.parse('el carrito contiene "{producto}"'))
def cart_contains(inventory_page, cart_page, producto):
    inventory_page.open_cart()
    assert producto in cart_page.item_names()
