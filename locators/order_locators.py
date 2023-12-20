from selenium.webdriver.common.by import By


class OrderPageLocators:
    title = By.CLASS_NAME, 'Order_Header__BZXOb'
    name_field = By.XPATH, ".//input[@placeholder='* Имя']"
    surname_field = By.XPATH, ".//input[@placeholder='* Фамилия']"
    address_field = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    metro_station_field = By.XPATH, ".//input[@placeholder='* Станция метро']"
    phone_number_field = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    next_button = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    date_field = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    duration = By.XPATH, ".//div[@class='Dropdown-control']"
    checkbox_black = By.ID, 'black'
    checkbox_grey = By.ID, 'grey'
    comment = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    option_24 = By.XPATH, ".//div[contains(text(), 'сутки')]"
    option_24_2 = By.XPATH, ".//div[contains(text(), 'двое суток')]"
    option_24_3 = By.XPATH, ".//div[contains(text(), 'трое суток')]"
    option_24_4 = By.XPATH, ".//div[contains(text(), 'четверо суток')]"
    option_24_5 = By.XPATH, ".//div[contains(text(), 'пятеро суток')]"
    option_24_6 = By.XPATH, ".//div[contains(text(), 'шестеро суток')]"
    option_24_7 = By.XPATH, ".//div[contains(text(), 'семеро суток')]"
    duration_options_list = [option_24, option_24_2, option_24_3, option_24_4, option_24_5, option_24_6, option_24_7]
    button_order_header = By.XPATH, ".//button[@class='Button_Button__ra12g']"
    button_order_content = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    popup_do_you_want = By.XPATH, ".//div[@class='Order_Modal__YZ-d3']"
    popup_yes = By.XPATH, ".//button[text()='Да']"
    popup_order_completed = By.XPATH, ".//div[text()='Заказ оформлен']"
    button_look_at_status = By.XPATH, ".//button[text()='Посмотреть статус']"
    img_samokat = By.XPATH, ".//img[@alt='Scooter']"
    img_yandex = By.XPATH, ".//img[@alt='Yandex']"
    dzen_menu = By.XPATH, ".//span[@class='navigation-tab__text-3z']"
    cross_icon = By.XPATH, ".//span[@class = 'fe07a1dcd fb6553f69 ib84c1291 nb95c600f']"
    dzen_header = By.ID, "dzen-header"
    dzen_lay = By.XPATH, ".//span[@tabindex='0']"






