import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.question_page_locators import QuestionPageLocators
from locators.base_locators import BaseLocators
from data import URLS
import allure
from pages.question_page import QuestionPage


class TestQuestions:

    i = 0

    @allure.title('Проверка соответствия текстов ответов на вопросы о важном')
    @pytest.mark.parametrize('question', QuestionPageLocators.questions)
    def test_is_text_the_same(self, driver, question):
        question_page = QuestionPage(driver)
        question_page.open_page(URLS.BASE_URL)
        question_page.wait_element_is_clickable(question)
        question_page.click_element(BaseLocators.accept_coockies)
        question_page.click_element(question)
        answer = QuestionPageLocators.question_texts_list[TestQuestions.i]
        TestQuestions.i += 1
        assert question_page.get_answer_text(question) == answer, \
            (f'Значение текста вопроса ожидалось: "{answer}", '
             f'получено "{question_page.get_answer_text(question)}"')
