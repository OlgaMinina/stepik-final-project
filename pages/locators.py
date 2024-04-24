from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[value='Add to basket']")
    ALERT_MESSAGE = (By.XPATH, "//div[@id='messages']//div[1]//div[1]")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "div[class = 'alertinner '] p strong")
