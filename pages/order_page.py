import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Fill the person  information with {name}, {surname}, {address}, {metro_station_name}, {phone_number}")
    def fill_the_person_form(self, name, surname, address, metro_station_name, phone_number):
        BasePage.enter_text(self, OrderPageLocators.name_field, name)
        BasePage.enter_text(self, OrderPageLocators.surname_field, surname)
        BasePage.enter_text(self, OrderPageLocators.address_field, address)
        BasePage.enter_text(self, OrderPageLocators.metro_station_field, metro_station_name)
        BasePage.enter_text(self, OrderPageLocators.metro_station_field, Keys.DOWN)
        BasePage.enter_text(self, OrderPageLocators.metro_station_field, Keys.ENTER)
        BasePage.enter_text(self, OrderPageLocators.phone_number_field, phone_number)

    @allure.step("Fill the rent form information with {date}, {duration_locator}, {selected_checkbox}, {comment}")
    def fill_the_rent_form(self, date, duration_locator, selected_checkbox, comment):
        BasePage.enter_text(self, OrderPageLocators.date_field, date)
        BasePage.enter_text(self, OrderPageLocators.date_field, Keys.ENTER)
        self.click_element(OrderPageLocators.duration)
        self.click_element(duration_locator)
        self.click_element(selected_checkbox)
        BasePage.enter_text(self, OrderPageLocators.comment, comment)





