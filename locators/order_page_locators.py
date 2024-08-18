from selenium.webdriver.common.by import By


class OrderPageLocators:
    START_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    FIRST_LIST = {
        'name': (By.XPATH, "//*[contains(@placeholder, '* Имя')]"),
        'soname': (By.XPATH, "//*[contains(@placeholder, '* Фамилия')]"),
        'addr': (By.XPATH, "//*[contains(@placeholder, '* Адрес: куда привезти заказ')]"),
        'metro': (By.XPATH, "//*[contains(@placeholder, '* Станция метро')]"),
        'phone': (By.XPATH, "//*[contains(@placeholder, '* Телефон: на него позвонит курьер')]")
    }

    SECOND_LIST = {
        'date': (By.XPATH, "//*[contains(@placeholder, '* Когда привезти самокат')]"),
        'period': (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"),
        'color': [
            (By.XPATH, "//input[@id='black']"),
            (By.XPATH, "//input[@id='grey']")
        ],
        'comment': (By.XPATH, "//*[contains(@placeholder, 'Комментарий для курьера')]")
    }

    FINISH_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Да']")
    ORDER_COMPLETE = (By.XPATH, "//div[contains(@class, 'Order') and text()='Заказ оформлен']")

    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]/img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]/img[@alt='Yandex']")

    DZEN_HEADER_LOGO = (By.XPATH, ".//*[contains(@class,'desktop-base-header__logoWithText')]")
