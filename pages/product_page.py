from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators


class Product(BasePage):

    def add_product(self):
        add = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add.click()

    def alert_success(self):
        assert "Coders at Work" == WebDriverWait(self.browser, 10). \
                 until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alertinner strong"))).text, "Error add"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is presented, but should not be"

    def disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), \
            "Success message is disappeared"