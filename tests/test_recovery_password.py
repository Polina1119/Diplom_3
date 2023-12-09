import allure
from pages.personal_account_page import PersonalAccountPage as LK
from pages.main_page import MainPage
from locators.recovery_password_locators import RecoveryPasswordPageLocators
from pages.recovery_password_page import RecoveryPasswordPage


class TestPasswordRecoveryPage:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_page_password_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lk()
        login_page = LK(driver)
        login_page.click_password_recovery()

        assert main_page.find_element(RecoveryPasswordPageLocators.PASSWORD_RECOVERY_TEXT).text == "Восстановление пароля"

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_click_to_button_restore(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lk()
        login_page = LK(driver)
        login_page.click_password_recovery()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.input_email()
        recovery_page.click_recovery_button()

        assert main_page.find_element(RecoveryPasswordPageLocators.SAVE).text == "Сохранить"

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_to_input(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_lk()
        login_page = LK(driver)
        login_page.click_password_recovery()
        recovery_page = RecoveryPasswordPage(driver)
        recovery_page.input_email()
        recovery_page.click_recovery_button()
        recovery_page.click_on_eye()

        assert main_page.find_element(RecoveryPasswordPageLocators.ACTIVE_PASSWORD)