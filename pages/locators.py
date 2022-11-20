from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    REG = (By.CSS_SELECTOR, "#registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    EMAIL_SING_IN = (By.CSS_SELECTOR, 'input#id_login-username.form-control')
    PASS_SING_IN = (By.CSS_SELECTOR, 'input#id_login-password.form-control')
    BTN_SING_IN = (By.CSS_SELECTOR, 'form#login_form > button.btn.btn-lg.btn-primary')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    EMAIL_SING_UP = (By.CSS_SELECTOR, 'input#id_registration-email.form-control')
    PASS_SING_UP_1 = (By.CSS_SELECTOR, 'input#id_registration-password1.form-control')
    PASS_SING_UP_2 = (By.CSS_SELECTOR, 'input#id_registration-password2.form-control')
    BTN_SING_UP = (By.CSS_SELECTOR, 'form#register_form > button.btn.btn-lg.btn-primary')

class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".product_main form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, 'div#content_inner > p')
    BASKET_FORM = (By.CSS_SELECTOR, '.basket-items')
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
