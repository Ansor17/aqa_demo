class CartPage:

    def __init__(self, page):
        self.page = page

    def validate_cart(self, expected_price):

        item_name = self.page.locator(
            ".inventory_item_name"
        ).inner_text()

        assert item_name == "Sauce Labs Backpack"

        item_price = self.page.locator(
            ".inventory_item_price"
        ).inner_text()

        assert item_price == expected_price

    def checkout(self):
        self.page.click("#checkout")