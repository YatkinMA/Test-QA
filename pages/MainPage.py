from pages.locator import MainPagesLocators
from .BasePage import BasePage
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPagesLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(*MainPagesLocators.LOGIN_LINK)
        self.browser.find_element(*MainPagesLocators.LOGIN_EMAIL)
        self.browser.find_element(*MainPagesLocators.LOGIN_PASSWORD)
        self.browser.find_element(*MainPagesLocators.LOGIN_BUTTON)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_EMAIL)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_PASSWORD)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_COFIRM_PASSWORD)
        self.browser.find_element(*MainPagesLocators.REGISTRATION_BUTTON)
        
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPagesLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser = self.browser, url = self.browser.current_url)
