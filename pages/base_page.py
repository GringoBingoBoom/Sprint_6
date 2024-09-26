import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def wait_element_clicable(self, element):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(element))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Проверка новых вкладок браузера, при наличии переключаемся в новую вкладку')
    def wait_and_switch_tab(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                self.wait_and_find_element(OrderPageLocators.DZEN_HEADER_LOGO)
                break
        return self.driver.current_url
