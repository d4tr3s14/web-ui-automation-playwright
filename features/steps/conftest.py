"""Step definitions COMPARTIDOS entre features (pytest-bdd los descubre vía conftest)."""
from __future__ import annotations

from pytest_bdd import given, parsers, when

from config import settings


@given("que inicié sesión como usuario estándar")
def logged_in(login_page, inventory_page):
    login_page.load()
    login_page.login(settings.STANDARD_USER, settings.PASSWORD)
    assert inventory_page.is_loaded(), "No se cargó la página de productos tras el login"


@when(parsers.parse('agrego "{producto}" al carrito'))
def add_product(inventory_page, producto):
    inventory_page.add_item_to_cart(producto)


@when("voy al carrito")
def go_to_cart(inventory_page):
    inventory_page.open_cart()
