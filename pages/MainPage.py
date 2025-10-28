from .BasePage import BasePage
from .login_page import LoginPage


# class MainPage(BasePage):
#     def go_to_login_page(self):
#         login_link = self.browser.find_element(*MainPagesLocators.LOGIN_LINK)
#         login_link.click()
#         alert = self.browser.switch_to.alert
#         alert.accept()


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
