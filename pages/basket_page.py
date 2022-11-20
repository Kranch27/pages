from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), \
            "Basket form present, but should not be"

    def should_be_text_basket_is_empty(self):
        assert 'empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text, \
            "Basket not empty, but should be"