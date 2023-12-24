from selenium.webdriver.common.by import By


class MainPageLocators:
    accept_coockies = By.ID, 'rcc-confirm-button'
    order_header_button = By.CLASS_NAME, 'Button_Button__ra12g'
    order_content_button = By.CLASS_NAME, 'Button_Middle__1CSJM'
    order_buttons = [order_header_button, order_content_button]
