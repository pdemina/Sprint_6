import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    firefox_driver = GeckoDriverManager().install()
    service = FS(firefox_driver)
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()
