from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(page):

    # LOGIN

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    print("Login successful")

    # INVENTORY

    inventory_page = InventoryPage(page)

    saved_price = inventory_page.add_backpack_to_cart()

    print("Product added")

    inventory_page.open_cart()

    # CART

    cart_page = CartPage(page)

    cart_page.validate_cart(saved_price)

    print("Cart validated")

    cart_page.checkout()

    # CHECKOUT

    checkout_page = CheckoutPage(page)

    checkout_page.fill_information()

    print("Checkout info filled")

    checkout_page.finish_order()

    checkout_page.validate_success()

    print("Order success")

    checkout_page.take_screenshot()

    print("Screenshot saved")