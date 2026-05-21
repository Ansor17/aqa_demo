class InventoryPage:

    def __init__(self, page):
        self.page = page

    def add_backpack_to_cart(self):

        backpack = self.page.locator(
            ".inventory_item"
        ).filter(
            has_text="Sauce Labs Backpack"
        )

        price = backpack.locator(
            ".inventory_item_price"
        ).inner_text()

        backpack.get_by_role(
            "button",
            name="Add to cart"
        ).click()

        return price

    def open_cart(self):
        self.page.click(".shopping_cart_link")