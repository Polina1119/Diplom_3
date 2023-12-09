from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountPageLocators as LK
import allure
import data


class PersonalAccountPage(BasePage):

    @allure.step('Нажимаем Войти')
    def click_on_login(self):
        self.find_element(LK.LOGIN_BUTTON).click()

    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_recovery(self):
        self.find_element(LK.RECOVERY_PASSWORD).click()

    @allure.step('Ввести email')
    def input_email(self):
        self.find_element(LK.EMAIL).send_keys(data.User.email)

    @allure.step('Ввести пароль')
    def input_password(self):
        self.find_element(LK.PASSWORD).send_keys(data.User.password)

    @allure.step('Кликнуть на кнопку "История заказов"')
    def click_button_history_orders(self):
        return self.find_element(LK.ORDERS_HISTORY).click()

    def get_order_number(self):
        return self.find_element(LK.ORDER_NUMBER).text

    @allure.step('Кликнуть по кнопке "Выход"')
    def click_logout_button(self):
        self.find_element(LK.EXIT).click()



