from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def wait_element_clicable(self, element):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(element))

