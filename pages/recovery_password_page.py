import allure
from locators.recovery_password_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage
import data


class RecoveryPasswordPage(BasePage):
    @allure.step('Ввод Email')
    def input_email(self):
        self.find_element(RecoveryPasswordPageLocators.EMAIL).send_keys(data.email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.find_element(RecoveryPasswordPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Кликнуть на кнопку показа или скрытия пароля')
    def click_on_eye(self):
        self.find_element(RecoveryPasswordPageLocators.SEE_PASSWORD).click()
