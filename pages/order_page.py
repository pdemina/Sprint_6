import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.order_locators import OrderPageLocators


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get the order url {url}")
    def get_order_url(self):
        url = self.get_current_url()
        return url

    @allure.step("Fill the person {name}")
    def fill_name(self, name):
        self.enter_text(OrderPageLocators.name_field, name)

    @allure.step("Fill the person {surname}")
    def fill_surname(self, surname):
        self.enter_text(OrderPageLocators.surname_field, surname)

    @allure.step("Fill the person {address}")
    def fill_address(self, address):
        self.enter_text(OrderPageLocators.address_field, address)

    @allure.step("Fill the person {metro_station_name}")
    def fill_metro_station_name(self, metro_station_name):
        self.enter_text(OrderPageLocators.metro_station_field, metro_station_name)
        self.enter_text(OrderPageLocators.metro_station_field, Keys.DOWN)
        self.enter_text(OrderPageLocators.metro_station_field, Keys.ENTER)

    @allure.step("Fill the person {phone_number}")
    def fill_phone_number(self, phone_number):
        self.enter_text(OrderPageLocators.phone_number_field, phone_number)

    @allure.step("Fill the rent {date}")
    def fill_date(self, date):
        self.enter_text(OrderPageLocators.date_field, date)
        self.enter_text(OrderPageLocators.date_field, Keys.ENTER)

    @allure.step("Fill the rent {duration_locator}")
    def fill_duration_locator(self, duration_locator):
        self.click_element(OrderPageLocators.duration)
        self.click_element(duration_locator)

    @allure.step("Tick the rent {selected_checkbox}")
    def tick_checkbox(self, selected_checkbox):
        self.click_element(selected_checkbox)

    @allure.step("Fill the rent {comment}")
    def fill_comment(self, comment):
        self.enter_text(OrderPageLocators.comment, comment)

    def fill_the_person_form(self, name, surname, address, metro_station_name, phone_number):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.fill_metro_station_name(metro_station_name)
        self.fill_phone_number(phone_number)

    @allure.step("Fill the rent form information with {date}, {duration_locator}, {selected_checkbox}, {comment}")
    def fill_the_rent_form(self, date, duration_locator, selected_checkbox, comment):
        self.fill_date(date)
        self.fill_duration_locator(duration_locator)
        self.tick_checkbox(selected_checkbox)
        self.fill_comment(comment)





