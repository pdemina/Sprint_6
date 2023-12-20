import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open {url} page")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Get element {locator}')
    def find_element(self, locator):
        element = self.wait_element_is_visible(locator)
        return self.driver.find_element(*locator)

    @allure.step('Enter text {text}')
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Wait element {locator}')
    def wait_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Wait element to be clickable {locator}')
    def wait_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Click element {locator}')
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Get Current URL')
    def get_current_url(self):
        return self.driver.current_url

