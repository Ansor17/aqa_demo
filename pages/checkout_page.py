class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def fill_information(self):

        self.page.fill("#first-name", "Ansor")
        self.page.fill("#last-name", "QA")
        self.page.fill("#postal-code", "734000")

        self.page.click("#continue")

    def finish_order(self):

        self.page.click("#finish")

    def validate_success(self):

        text = self.page.locator(
            ".complete-header"
        ).inner_text()

        assert text == "Thank you for your order!"

    def take_screenshot(self):

        self.page.screenshot(
            path="screenshots/final_page.png"
        )