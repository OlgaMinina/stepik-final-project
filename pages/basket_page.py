from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Item is presented, but should not"

    def should_be_message_that_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_CART), "The message is not present"
