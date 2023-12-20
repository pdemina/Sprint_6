import pytest
import allure
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.order_locators import OrderPageLocators
from data import URLS


class TestOrderButtons:

    @allure.title('Кнопка Заказать перенаправляет пользователя на форму заказа')
    @allure.description('Проверка кнопки в header и content')
    @pytest.mark.parametrize('order_button', BaseLocators.order_buttons)
    def test_order_buttons_redirect(self, driver, order_button):
        base_page = BasePage(driver)
        base_page.open_page(URLS.BASE_URL)
        base_page.click_element(BaseLocators.accept_coockies)
        if BaseLocators.order_buttons == BaseLocators.order_content_button:
            base_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        base_page.wait_element_is_visible(order_button)
        base_page.click_element(order_button)
        base_page.wait_element_is_visible(OrderPageLocators.title)
        assert base_page.driver.current_url == URLS.ORDER_URL, (f'Значение URL ожидалось: "{URLS.ORDER_URL}", '
                                                                f'получено "{base_page.driver.current_url}"')
