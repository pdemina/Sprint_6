import allure
from locators.main_locators import MainPageLocators
from locators.order_locators import OrderPageLocators
from data import URLS
from pages.order_page import OrderPage


class TestOrderButtons:

    @allure.title('Кнопка Заказать перенаправляет пользователя на форму заказа')
    @allure.description('Проверка кнопки в header')
    def test_order_header_button_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(MainPageLocators.accept_coockies)
        order_page.wait_element_is_visible_and_click(MainPageLocators.order_header_button)
        order_page.wait_element_is_visible(OrderPageLocators.title)
        assert order_page.driver.current_url == URLS.ORDER_URL, (f'Значение URL ожидалось: "{URLS.ORDER_URL}", '
                                                                 f'получено "{order_page.driver.current_url}"')

    @allure.title('Кнопка Заказать перенаправляет пользователя на форму заказа')
    @allure.description('Проверка кнопки в content')
    def test_order_content_button_redirect(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(MainPageLocators.accept_coockies)
        order_page.scroll_to_body()
        order_page.wait_element_is_visible_and_click(MainPageLocators.order_content_button)
        order_page.wait_element_is_visible(OrderPageLocators.title)
        assert order_page.driver.current_url == URLS.ORDER_URL, (f'Значение URL ожидалось: "{URLS.ORDER_URL}", '
                                                                 f'получено "{order_page.driver.current_url}"')
