from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_invalid_login(page):
    log_in_page = LoginPage(page)
    log_in_page.login(username="sowmya.ala@gmail.com", password="SOwmya123")
    log_in_page.assert_login_failed()
