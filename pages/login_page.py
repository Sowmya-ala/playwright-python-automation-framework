from playwright.sync_api import Page, expect

from pages import dashboard_page
from pages.dashboard_page import DashboardPage


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.email = "#userEmail"
        self.password = "#userPassword"
        self.loginbtn = "#login"
        self.toast = ".toast-message"

    def login(self, username, password):
        self.page.locator(self.email).fill(username)
        self.page.locator(self.password).fill(password)
        self.page.locator(self.loginbtn).click()
        return DashboardPage(self.page)

    def assert_login_failed(self):
        error_message = self.page.locator(".toast-message")
        expect(self.page.locator(self.toast)).to_have_text("Incorrect email or password.")


