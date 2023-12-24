import pytest
import allure
from locators.main_locators import MainPageLocators
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
        order_page.click_element(MainPageLocators.accept_coockies)
        order_page.wait_element_is_visible(MainPageLocators.order_header_button)
        order_page.click_element(MainPageLocators.order_header_button)
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
        order_page.click_element(MainPageLocators.accept_coockies)
        order_page.wait_element_is_visible(MainPageLocators.order_header_button)
        order_page.click_element(MainPageLocators.order_header_button)
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


