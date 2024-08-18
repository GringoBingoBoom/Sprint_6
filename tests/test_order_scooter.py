import pytest
from data import Urls, OrderScooter
import allure
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestMainQuestions:

    @allure.title('2.1 Заказ самоката. Создание заказа')
    @allure.description('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.')
    @pytest.mark.parametrize('user_data', OrderScooter.order_data_1st_page)
    def test_scooter_order_fill_order_fields_and_check_order_complete(self, driver, user_data):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.SCOOTER)
        order_page.wait_and_click(OrderPageLocators.START_ORDER_BUTTON)
        order_page.fill_first_order_list(user_data)
        order_page.fill_second_order_list(user_data)

        assert 'Заказ оформлен' in order_page.wait_and_find_element(OrderPageLocators.ORDER_COMPLETE).text, (
            "Заказ не был успешно завершен, нет подтверждения"
        )

    @allure.title('2.2 Заказ самоката. Нажать на логотип «Самоката»/Яндекса')
    @allure.description('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».'
                        'Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная'
                        ' страница Дзена')
    @pytest.mark.parametrize('locator, target_url', [[OrderPageLocators.SCOOTER_LOGO, Urls.SCOOTER],
                                                     [OrderPageLocators.YANDEX_LOGO, Urls.DZEN]])
    def test_logo_redirect_to_target_page(self, driver, locator, target_url):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.SCOOTER)
        order_page.wait_and_click(OrderPageLocators.START_ORDER_BUTTON)
        order_page.wait_and_click(locator)

        assert order_page.wait_and_switch_tab() == target_url, 'Переход по ссылке не выполнен успешно'
