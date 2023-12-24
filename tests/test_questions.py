import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.question_page_locators import QuestionPageLocators
from locators.main_locators import MainPageLocators
from data import URLS
import allure
from pages.question_page import QuestionPage
from data import QuestionTexts


class TestQuestions:

    @allure.title('Проверка соответствия текстов ответов на вопросы о важном')
    @pytest.mark.parametrize('question, text', [
                             [QuestionPageLocators.question_payment, QuestionTexts.question_payment_text],
                             [QuestionPageLocators.question_more_scooters, QuestionTexts.question_more_scooters_text],
                             [QuestionPageLocators.question_time_of_rent, QuestionTexts.question_time_of_rent_text],
                             [QuestionPageLocators.question_order_today, QuestionTexts.question_order_today_text],
                             [QuestionPageLocators.question_extend_or_cancel_earlier, QuestionTexts.question_extend_or_cancel_earlier_text],
                             [QuestionPageLocators.question_charge, QuestionTexts.question_charge_text],
                             [QuestionPageLocators.question_cancel_order, QuestionTexts.question_cancel_order_text],
                             [QuestionPageLocators.question_mka, QuestionTexts.question_mkad_text]]
                             )
    def test_is_text_the_same(self, driver, question, text):
        question_page = QuestionPage(driver)
        question_page.open_page(URLS.BASE_URL)
        question_page.wait_element_is_clickable(question)
        question_page.click_element(MainPageLocators.accept_coockies)
        question_page.click_element(question)
        assert question_page.get_answer_text(question) == text, \
            (f'Значение текста вопроса ожидалось: "{text}", '
             f'получено "{question_page.get_answer_text(question)}"')
