"""Steps del feature de compra end-to-end."""
from __future__ import annotations

from pytest_bdd import parsers, scenarios, then, when

scenarios("checkout.feature")


@when(parsers.parse(
    'procedo al pago con nombre "{first}" apellido "{last}" y código postal "{zip_code}"'
))
def proceed_to_payment(cart_page, checkout_page, first, last, zip_code):
    cart_page.checkout()
    checkout_page.fill_information(first, last, zip_code)
    checkout_page.continue_to_summary()


@when("continúo el checkout sin completar el nombre")
def continue_without_first_name(cart_page, checkout_page):
    cart_page.checkout()
    checkout_page.fill_information("", "Lovelace", "12345")
    checkout_page.continue_to_summary()


@when("finalizo la compra")
def finish_purchase(checkout_page):
    checkout_page.finish()


@then(parsers.parse('veo la confirmación "{mensaje}"'))
def see_confirmation(checkout_page, mensaje):
    assert checkout_page.is_complete()
    assert mensaje in checkout_page.success_message()


@then(parsers.parse('veo el error de checkout "{mensaje}"'))
def see_checkout_error(checkout_page, mensaje):
    assert mensaje in checkout_page.error_message()


@then("el total del pedido es igual al subtotal más los impuestos")
def total_is_consistent(checkout_page):
    esperado = round(checkout_page.item_total() + checkout_page.tax(), 2)
    assert checkout_page.total() == esperado, (
        f"Total inconsistente: subtotal {checkout_page.item_total()} "
        f"+ impuestos {checkout_page.tax()} != total {checkout_page.total()}"
    )
