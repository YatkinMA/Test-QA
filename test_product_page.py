from pages.MainPage import MainPage
from pages.BasePage import BasePage
import pytest, time
from pages.product_page import ProductPage, ProductPageLocators


# @pytest.mark.parametrize(
#     "link",
#     [
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
#     ],
# )
@pytest.mark.parametrize(
    "link",
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"],
)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = MainPage(browser, link)
#     page.open()
#     page.add_product_in_basket()
#     page.solve_quiz_and_get_code()
#     # time.sleep(5000)
#     page.check_product_name_add_in_basket()
#     page.check_product_price_add_in_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = MainPage(browser, link)
    # Открываем страницу товара
    page.open()
    # Добавляем товар в корзину
    page.add_product_in_basket()
    # page.solve_quiz_and_get_code()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE
    ), "Success message is presented, but should not be test1"


@pytest.mark.parametrize(
    "link",
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"],
)
def test_guest_cant_see_success_message(browser, link):
    page = MainPage(browser, link)
    # Открываем страницу товара
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE
    ), "Success message is presented, but should not be test2"


@pytest.mark.parametrize(
    "link",
    ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"],
)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = MainPage(browser, link)
    # Открываем страницу товара
    page.open()
    # Добавляем товар в корзину
    page.add_product_in_basket()
    # page.solve_quiz_and_get_code()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    assert page.is_disappeared(
        *ProductPageLocators.SUCCESS_MESSAGE
    ), "Success message is presented, but should not be test3"

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()