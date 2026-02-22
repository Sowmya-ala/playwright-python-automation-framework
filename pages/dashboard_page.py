import re

from playwright.sync_api import Page, expect




class DashboardPage:
    def __init__(self, page:Page):
        self.page = page

    def is_loaded(self):
        expect(self.page).to_have_url(re.compile("dashboard"))

    def has_products(self):
        products = self.page.locator(".card")
        expect(products.first).to_be_visible()