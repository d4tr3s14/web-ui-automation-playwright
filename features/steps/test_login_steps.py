"""Steps del feature de inicio de sesión."""
from __future__ import annotations

from pytest_bdd import given, parsers, scenarios, then, when

from config import settings

scenarios("login.feature")


@given("que estoy en la página de inicio de sesión")
def open_login(login_page):
    login_page.load()


@when("inicio sesión con el usuario estándar")
def login_standard(login_page):
    login_page.login(settings.STANDARD_USER, settings.PASSWORD)


@when("inicio sesión con el usuario bloqueado")
def login_locked(login_page):
    login_page.login(settings.LOCKED_USER, settings.PASSWORD)


@when(parsers.parse('inicio sesión con usuario "{usuario}" y contraseña "{password}"'))
def login_custom(login_page, usuario, password):
    login_page.login(usuario, password)


@then("veo la página de productos")
def see_products(inventory_page):
    assert inventory_page.is_loaded()


@then(parsers.parse('veo el mensaje de error "{mensaje}"'))
def see_specific_error(login_page, mensaje):
    assert mensaje in login_page.error_message()


@then("veo un mensaje de error")
def see_any_error(login_page):
    assert login_page.has_error()
