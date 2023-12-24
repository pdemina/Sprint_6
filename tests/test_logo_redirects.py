import allure
from locators.main_locators import MainPageLocators
from locators.order_locators import OrderPageLocators
from data import URLS
from pages.order_page import OrderPage


class TestLogoRedirections:

    @allure.title('Проверка редиректа по клику на логотип самоката')
    @allure.description('Проверка редиректа на https://qa-scooter.praktikum-services.ru/ при нажатии на лого самоката')
    def test_successful_redirect_samokat_click(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(MainPageLocators.accept_coockies)
        order_page.wait_element_is_visible(MainPageLocators.order_header_button)
        order_page.click_element(MainPageLocators.order_header_button)
        order_page.click_element(OrderPageLocators.img_samokat)
        order_page.wait_element_is_visible(MainPageLocators.order_header_button)
        assert order_page.get_current_url() == URLS.BASE_URL, (f'Значение URL ожидалось: "{URLS.BASE_URL}", '
                                                               f'получено: "{order_page.get_current_url()}"')

    @allure.title('Проверка редиректа по клику на логотип дзена')
    @allure.description('Проверка редиректа на https://dzen.ru/?yredirect=true при нажатии на лого дзена')
    def test_successful_redirect_yandex_click(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(MainPageLocators.accept_coockies)
        order_page.wait_element_is_visible(MainPageLocators.order_header_button)
        order_page.click_element(OrderPageLocators.img_yandex)
        order_page.switch_tab()
        order_page.click_element(OrderPageLocators.dzen_lay)
        assert order_page.get_current_url() == URLS.DZEN_URL, (f'Значение URL ожидалось: "{URLS.DZEN_URL}", '
                                                               f'получено: "{order_page.get_current_url()}"')
