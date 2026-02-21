from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_valid_login(page: Page):
    log_in_page = LoginPage(page)
    log_in_page.login(username="sowmya.ala@gmail.com", password="Nirvan123")
    expect(page).to_have_url("https://rahulshettyacademy.com/client/#/dashboard/dash")
    products = page.locator(".card")
    expect(products.first).to_be_visible()
