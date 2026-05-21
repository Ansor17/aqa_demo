from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")