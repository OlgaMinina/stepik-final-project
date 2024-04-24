from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click()

    def should_be_product_added(self):
        product_name = self.extraction_product_name()
        product_price = self.extraction_product_price()

        self.should_be_same_name(product_name)
        self.should_be_same_price(product_price)

    def extraction_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def extraction_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_same_name(self, product_name):
        message_text = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE).text
        assert product_name in message_text, "Product name does not match"

    def should_be_same_price(self, product_price):
        price_text = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        assert product_price == price_text, "Product price does not match"

