from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click()

    def should_be_product_added(self):
        self.should_be_same_name()
        self.should_be_same_price()

    def should_be_same_name(self):
        message_text = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE).text
        assert "The shellcoder's handbook" in message_text

    def should_be_same_price(self):
        price_text = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert "£9.99" == price_text

