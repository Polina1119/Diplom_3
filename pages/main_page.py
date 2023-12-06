from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as Main
import allure


class MainPage(BasePage):
    @allure.step('Нажимаем на Конструктор')
    def click_on_constructor(self):
        return self.find_element(Main.CONSTRUCTOR).click()

    @allure.step('Нажимаем на Лента заказов')
    def click_on_order_feed(self):
        return self.find_element(Main.ORDER_FEED).click()

    @allure.step('Нажимаем на игредиент')
    def click_on_ingredient(self):
        return self.find_element(Main.FLUORESCENT_BUN).click()

    @allure.step('Скролл до ингредиента')
    def scroll(self):
        element = self.find_element(Main.FLUORESCENT_BUN)
        return self.execute_script(element)

    @allure.step('Нажимаем на крестик')
    def close_window(self):
        return self.find_element(Main.CLOSE).click()

    @allure.step('Нажимаем на Личный кабинет')
    def click_on_lk(self):
        return self.find_element(Main.LK).click()

    @allure.step('Нажимаем на Оформить заказ')
    def click_on_place_order(self):
        return self.find_element(Main.PLACE_ORDER).click()

    @allure.step('Проверяем счетчик ингредиента')
    def check_counter_ingredients(self):
        return self.find_element(Main.COUNTER_INGREDIENTS).text

    @allure.step('Перемещаем ингредиент в заказ')
    def move_ingredient_in_order(self, locator_1, locator_2):
        self.drag_and_drop_on_element(locator_1, locator_2)

    @allure.step('Проверяем номер заказа')
    def check_order_number(self):
        return self.find_element(Main.ORDER_NUMBER).text



