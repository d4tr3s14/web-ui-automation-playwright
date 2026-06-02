"""Step definitions COMPARTIDOS entre features (pytest-bdd los descubre vía conftest)."""
from __future__ import annotations

from pytest_bdd import given, parsers, then, when

from config import settings


# --------------------------------------------------------------------------- #
# Given
# --------------------------------------------------------------------------- #
@given("que inicié sesión como usuario estándar")
def logged_in(login_page, inventory_page):
    login_page.load()
    login_page.login(settings.STANDARD_USER, settings.PASSWORD)
    assert inventory_page.is_loaded(), "No se cargó la página de productos tras el login"


# --------------------------------------------------------------------------- #
# When
# --------------------------------------------------------------------------- #
@when(parsers.parse('agrego "{producto}" al carrito'))
def add_product(inventory_page, producto):
    inventory_page.add_item_to_cart(producto)


@when(parsers.parse('quito "{producto}" del carrito'))
def remove_product(inventory_page, producto):
    inventory_page.remove_item_from_cart(producto)


@when("voy al carrito")
def go_to_cart(inventory_page):
    inventory_page.open_cart()


# --------------------------------------------------------------------------- #
# Then
# --------------------------------------------------------------------------- #
@then(parsers.parse("el contador del carrito muestra {n:d}"))
def cart_badge_shows(inventory_page, n):
    assert inventory_page.cart_count() == n


@then(parsers.parse('el carrito contiene "{producto}"'))
def cart_contains(inventory_page, cart_page, producto):
    inventory_page.open_cart()
    assert producto in cart_page.item_names()
