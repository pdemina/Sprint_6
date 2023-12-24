import allure
from pages.base_page import BasePage


class QuestionPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get answer of question {question}")
    def get_answer_text(self, question):
        found_element = self.find_element(question)
        text = found_element.text
        return text






