import pytest
import allure
from locators.base_locators import BaseLocators
from locators.order_locators import OrderPageLocators
from data import URLS
from pages.order_page import OrderPage


class TestOrderCreation:

    @allure.title('Проверка наличия попапа после нажатия кнопки заказать в секции header')
    @allure.description('Проверка осуществляется с двумя наборами данных')
    @pytest.mark.parametrize('name, surname, address, metro_station_name, phone_number, date, duration_locator, selected_checkbox, comment',
                             [['Алёна', 'Иванова', 'Ленина 10', 'Чистые пруды', '+79007009876', '22.03.1994', OrderPageLocators.option_24_2, OrderPageLocators.checkbox_grey, 'первый подъезд'],
                              ['Ирина', 'Кузнецова', 'Кирова 5', 'Сокольники', '+79337779975', '20.02.2001', OrderPageLocators.option_24_2, OrderPageLocators.checkbox_black, 'не торопитесь']])
    def test_successful_order_header_order_button(self, driver, name, surname, address, metro_station_name, phone_number, date, duration_locator, selected_checkbox, comment):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(BaseLocators.accept_coockies)
        order_page.wait_element_is_visible(BaseLocators.order_header_button)
        order_page.click_element(BaseLocators.order_header_button)
        order_page.wait_element_is_visible(OrderPageLocators.title)
        order_page.fill_the_person_form(name, surname, address, metro_station_name, phone_number)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.wait_element_is_visible(OrderPageLocators.date_field)
        order_page.fill_the_rent_form(date, duration_locator, selected_checkbox, comment)
        order_page.click_element(OrderPageLocators.button_order_header)
        order_page.wait_element_is_visible(OrderPageLocators.popup_do_you_want)
        order_page.click_element(OrderPageLocators.popup_yes)
        assert order_page.find_element(OrderPageLocators.popup_do_you_want), f'Попап c номером заказа не обнаружен'

    @allure.title('Проверка наличия попапа после нажатия кнопки заказать в секции контента')
    @allure.description('Проверка осуществляется с двумя наборами данных')
    @pytest.mark.parametrize('name, surname, address, metro_station_name, phone_number, date, duration_locator, selected_checkbox, comment',
                             [['Алёна', 'Иванова', 'Ленина 10', 'Чистые пруды', '+79007009876', '22.03.1994', OrderPageLocators.option_24_2, OrderPageLocators.checkbox_grey, 'первый подъезд'],
                              ['Ирина', 'Кузнецова', 'Кирова 5', 'Сокольники', '+79337779975', '20.02.2001', OrderPageLocators.option_24_2, OrderPageLocators.checkbox_black, 'не торопитесь']])
    def test_successful_order_content_order_button(self, driver, name, surname, address, metro_station_name, phone_number, date, duration_locator, selected_checkbox, comment):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(BaseLocators.accept_coockies)
        order_page.wait_element_is_visible(BaseLocators.order_header_button)
        order_page.click_element(BaseLocators.order_header_button)
        order_page.wait_element_is_visible(OrderPageLocators.title)
        order_page.fill_the_person_form(name, surname, address, metro_station_name, phone_number)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.wait_element_is_visible(OrderPageLocators.date_field)
        order_page.fill_the_rent_form(date, duration_locator, selected_checkbox, comment)
        order_page.click_element(OrderPageLocators.button_order_content)
        order_page.wait_element_is_visible(OrderPageLocators.popup_do_you_want)
        order_page.click_element(OrderPageLocators.popup_yes)
        order_page.wait_element_is_visible(OrderPageLocators.popup_order_completed)
        assert order_page.find_element(OrderPageLocators.popup_order_completed), f'Попап c номером заказа не обнаружен'

    @allure.title('Проверка редиректа по клику на логотип самоката')
    @allure.description('Проверка редиректа на https://qa-scooter.praktikum-services.ru/ при нажатии на лого самоката')
    @pytest.mark.parametrize(
        'name, surname, address, metro_station_name, phone_number, date, duration_locator, selected_checkbox, comment',
        [['Алёна', 'Иванова', 'Ленина 10', 'Чистые пруды', '+79007009876', '22.03.1994', OrderPageLocators.option_24_2,
          OrderPageLocators.checkbox_grey, 'первый подъезд']
         ])
    def test_successful_redirect_samokat_click(self, driver, name, surname, address, metro_station_name, phone_number,
                                               date, duration_locator, selected_checkbox, comment):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(BaseLocators.accept_coockies)
        order_page.wait_element_is_visible(BaseLocators.order_header_button)
        order_page.click_element(BaseLocators.order_header_button)
        order_page.wait_element_is_visible(OrderPageLocators.title)
        order_page.fill_the_person_form(name, surname, address, metro_station_name, phone_number)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.wait_element_is_visible(OrderPageLocators.date_field)
        order_page.fill_the_rent_form(date, duration_locator, selected_checkbox, comment)
        order_page.click_element(OrderPageLocators.button_order_content)
        order_page.wait_element_is_visible(OrderPageLocators.popup_do_you_want)
        order_page.click_element(OrderPageLocators.popup_yes)
        order_page.wait_element_is_visible(OrderPageLocators.popup_order_completed)
        order_page.click_element(OrderPageLocators.button_look_at_status)
        order_page.click_element(OrderPageLocators.img_samokat)
        order_page.wait_element_is_visible(BaseLocators.order_header_button)
        assert order_page.driver.current_url == URLS.BASE_URL, (f'Значение URL ожидалось: "{URLS.BASE_URL}", '
                                                                f'получено: "{order_page.driver.current_url}"')

    @allure.title('Проверка редиректа по клику на логотип дзена')
    @allure.description('Проверка редиректа на https://dzen.ru/?yredirect=true при нажатии на лого дзена')
    @pytest.mark.parametrize('name, surname, address, metro_station_name, phone_number, date, duration_locator, selected_checkbox, comment',
            [['Алёна', 'Иванова', 'Ленина 10', 'Чистые пруды', '+79007009876', '22.03.1994',OrderPageLocators.option_24_2,
              OrderPageLocators.checkbox_grey, 'первый подъезд']])
    def test_successful_redirect_yandex_click(self, driver, name, surname, address, metro_station_name, phone_number,
                                              date, duration_locator, selected_checkbox, comment):
        order_page = OrderPage(driver)
        order_page.open_page(URLS.BASE_URL)
        order_page.click_element(BaseLocators.accept_coockies)
        order_page.wait_element_is_visible(BaseLocators.order_header_button)
        order_page.click_element(BaseLocators.order_header_button)
        order_page.wait_element_is_visible(OrderPageLocators.title)
        order_page.fill_the_person_form(name, surname, address, metro_station_name, phone_number)
        order_page.click_element(OrderPageLocators.next_button)
        order_page.wait_element_is_visible(OrderPageLocators.date_field)
        order_page.fill_the_rent_form(date, duration_locator, selected_checkbox, comment)
        order_page.click_element(OrderPageLocators.button_order_content)
        order_page.wait_element_is_visible(OrderPageLocators.popup_do_you_want)
        order_page.click_element(OrderPageLocators.popup_yes)
        order_page.wait_element_is_visible(OrderPageLocators.popup_order_completed)
        order_page.click_element(OrderPageLocators.button_look_at_status)
        order_page.click_element(OrderPageLocators.img_yandex)
        order_page.driver.switch_to.window(order_page.driver.window_handles[1])
        order_page.click_element(OrderPageLocators.dzen_lay)
        assert order_page.driver.current_url == URLS.DZEN_URL, (f'Значение URL ожидалось: "{URLS.DZEN_URL}", '
                                                                f'получено: "{order_page.driver.current_url}"')
