import pytest
from data import Urls
import allure

from locators.main_page_locators import Questions
from pages.main_page import MainPage


class TestMainQuestions:

    @allure.title('1. Проверка «Вопросы о важном»')
    @allure.description('Проверка выпадающего списока в разделе «Вопросы о важном». '
                        'когда нажимаешь на стрелочку, открывается соответствующий текст')
    @pytest.mark.parametrize('question, answer', zip(Questions.QUESTIONS, Questions.ANSWERS))
    def test_main_questions_check_answers_correct(self, driver, question, answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.SCOOTER)

        question_locator = main_page.create_locator_by_text(Questions.TEMPLATE, question)
        answer_locator = main_page.create_locator_by_text(Questions.TEMPLATE, answer)

        main_page.scroll_and_click(question_locator)
        assert main_page.wait_and_get_text(answer_locator) == answer, (
            "Текст ответа не отображается при нажатии на вопрос")
