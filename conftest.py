import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    service = Service("/snap/bin/firefox.geckodriver")
    firefox = webdriver.Firefox(service=service)
    firefox.maximize_window()

    yield firefox

    firefox.quit()
