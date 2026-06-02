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


@when("finalizo la compra")
def finish_purchase(checkout_page):
    checkout_page.finish()


@then(parsers.parse('veo la confirmación "{mensaje}"'))
def see_confirmation(checkout_page, mensaje):
    assert checkout_page.is_complete()
    assert mensaje in checkout_page.success_message()
