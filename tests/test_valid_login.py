from playwright.sync_api import expect

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


def test_valid_login(page):
    log_in_page = LoginPage(page)
    log_in_page.login(username="sowmya.ala@gmail.com", password="Nirvan123")

    #dash board page validation
    dashboard_page = DashboardPage(page)
    dashboard_page.is_loaded()
    dashboard_page.has_products()



