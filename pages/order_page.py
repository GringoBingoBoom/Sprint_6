import allure
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Поиск кнопки Заказ и клик по ней.')
    def wait_and_click(self, locator):
        element = self.find_element(locator)
        self.wait_element_clicable(element)
        element.click()

    @allure.step('Заполнение 1-ой страницы заказа')
    def fill_first_order_list(self, user_data):
        locators = OrderPageLocators.FIRST_LIST
        for key in locators:
            self.find_and_send(locators[key], user_data[key])
            if key == 'metro':
                self.wait_and_click((By.XPATH, f"//*[text()='{user_data['metro']}']"))
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнение 2-ой страницы заказа')
    def fill_second_order_list(self, user_data):
        locators = OrderPageLocators.SECOND_LIST
        self.find_and_send(locators['date'], user_data['date'])
        if user_data['color'] == 'чёрный жемчуг':
            self.wait_and_click(locators['color'][0])  # 'чёрный жемчуг'
        else:
            self.wait_and_click(locators['color'][1])  # 'серая безысходность'
        self.find_and_send(locators['comment'], user_data['comment'])
        self.wait_and_click(locators['period'])
        self.wait_and_click((By.XPATH, f"//div[@class='Dropdown-option' and text()='{user_data['period']}']"))

        self.wait_and_click(OrderPageLocators.FINISH_ORDER_BUTTON)
        self.wait_and_click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Поиск поля заказа и заполнение значением первой страницы заказа')
    def find_and_send(self, locator, user_data):
        self.wait_and_find_element(locator).send_keys(user_data)
