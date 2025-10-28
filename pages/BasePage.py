from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.product_page import BasePageLocators
from pages.locator import MainPagesLocators
from pages.product_page import ProductPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(
                self.browser,
                timeout,
                poll_frequency=1,
                ignored_exceptions=[TimeoutException],
            ).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    # def should_be_login_link(self):
    #     assert self.is_element_present(
    #         *BasePageLocators.LOGIN_LINK
    #     ), "Login link is not presented"

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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"
