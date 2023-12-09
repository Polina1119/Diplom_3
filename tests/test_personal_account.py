import allure
from pages.personal_account_page import PersonalAccountPage as LK
from locators.personal_account_locators import PersonalAccountPageLocators as LK_locators
from pages.main_page import MainPage


class TestAccountProfilePage:

    def test_go_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_lk()

        assert main_page.find_element(LK_locators.EXIT).text == 'Выход'

    @allure.title('Переход в раздел "История заказов"')
    def test_go_to_history_orders(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_lk()
        lk = LK(driver)
        lk.click_button_history_orders()

        assert main_page.current_url() == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_lk()
        lk = LK(driver)
        lk.click_logout_button()

        assert main_page.find_element(LK_locators.LOGIN_BUTTON).text == 'Войти'
