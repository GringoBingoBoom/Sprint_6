import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocator
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Ожидание загрузки на главной. Скроллиг до элемента и клик по нему.')
    def scroll_and_click(self, locator):
        self.wait_and_find_element(MainPageLocator.HOME_HEADER)  # ждем появление заголовка на главной
        element = self.find_element(locator)
        self.scroll_to_element(element)
        self.wait_element_clicable(element)
        element.click()

    @allure.step('Создание локатора по тексту вопроса или ответа по шаблону')
    def create_locator_by_text(self, template, text):
        return (template[0], template[1].substitute(text=text))

    @allure.step('Ожидание элемента и возвращение текста')
    def wait_and_get_text(self, locator):
        return self.wait_and_find_element(locator).text
