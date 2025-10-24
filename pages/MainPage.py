from pages.locator import MainPagesLocators
from pages.product_page import ProductPageLocators
from .BasePage import BasePage
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPagesLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        self.browser.find_element(*MainPagesLocators.LOGIN_LINK)
        self.browser.find_element(*MainPagesLocators.LOGIN_EMAIL)
        self.browser.find_element(*MainPagesLocators.LOGIN_PASSWORD)
        self.browser.find_element(*MainPagesLocators.LOGIN_BUTTON)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_EMAIL)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_PASSWORD)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_COFIRM_PASSWORD)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_BUTTON)

    def add_product_in_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_product_name_add_in_basket(self):
        list_strong = self.browser.find_elements(
            *ProductPageLocators.CHECK_PRODUCT_NAME_AND_PRICE_IN_SUCCESS_MESSAGE
        )
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        found = False
        for message in list_strong:
            if message.text == book_name:
                found = True
                break
        assert found, "Book name not found in messages"


    def check_product_price_add_in_basket(self):
        list_strong = self.browser.find_elements(
            *ProductPageLocators.CHECK_PRODUCT_NAME_AND_PRICE_IN_SUCCESS_MESSAGE
        )
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        found = False
        for message in list_strong:
            if message.text == book_price:
                found = True
                break
        assert found, "Book price not found in messages"
