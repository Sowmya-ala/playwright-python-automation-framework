import re

from playwright.sync_api import Page, expect




class DashboardPage:
    def __init__(self, page:Page):
        self.page = page

    def is_loaded(self):
        expect(self.page).to_have_url(re.compile("dashboard"))

    def assert_product_count(self):
        products = self.page.locator(".card")
        expect(products).to_have_count(3)

    def add_product_to_cart(self, product_name):
        cards = self.page.locator(".card")
        count = cards.count()
        for i in range(count):
            card = cards.nth(i)  # keep the locator
            name = card.locator("b").text_content().strip()  # get only product name

            if name == product_name:
                card.get_by_role("button", name="Add To Cart").click()
                return
        raise AssertionError(f"Product not found: {product_name}")



