"""Steps del feature de catálogo de productos."""
from __future__ import annotations

from pytest_bdd import parsers, scenarios, then, when

scenarios("inventory.feature")


@when(parsers.parse('ordeno los productos por "{criterio}"'))
def sort_products(inventory_page, criterio):
    inventory_page.sort_by(criterio)


@then(parsers.parse("el catálogo muestra {n:d} productos"))
def catalog_shows(inventory_page, n):
    assert inventory_page.product_count() == n


@then("los precios quedan ordenados de menor a mayor")
def prices_ascending(inventory_page):
    precios = inventory_page.prices()
    assert precios == sorted(precios), f"Los precios no están en orden ascendente: {precios}"


@then("los nombres quedan ordenados de la Z a la A")
def names_descending(inventory_page):
    nombres = inventory_page.product_names()
    assert nombres == sorted(nombres, reverse=True), f"Los nombres no están en orden Z-A: {nombres}"
