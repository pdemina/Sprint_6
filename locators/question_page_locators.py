from selenium.webdriver.common.by import By


class QuestionPageLocators:
    question_payment = By.ID, 'accordion__heading-0' #Сколько это стоит? И как оплатить?
    question_more_scooters = By.ID, 'accordion__heading-1' #Хочу сразу несколько самокатов! Так можно?
    question_time_of_rent = By.ID, 'accordion__heading-2' #Как рассчитывается время аренды?
    question_order_today = By.ID, 'accordion__heading-3' #Можно ли заказать самокат прямо на сегодня?
    question_extend_or_cancel_earlier = By.ID, 'accordion__heading-4' #Можно ли продлить заказ или вернуть самокат раньше?
    question_charge = By.ID, 'accordion__heading-5' #Вы привозите зарядку вместе с самокатом?
    question_cancel_order = By.ID, 'accordion__heading-6' #Можно ли отменить заказ?
    question_mka = By.ID, 'accordion__heading-7' #Я живу за МКАДом, привезёте?
    questions_accordion = By.CLASS_NAME, 'Home_FAQ__3uVm4' #accordion
    questions = [question_payment, question_more_scooters, question_time_of_rent, question_order_today,
                 question_extend_or_cancel_earlier, question_charge, question_cancel_order, question_mka] #список вопросов для параметризации
