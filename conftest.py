import pytest
from config.config import BASE_URL

@pytest.fixture(scope="function")
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(BASE_URL)

    yield page

    browser.close()