import allure
from selenium.webdriver.common.by import By
from locators.order_feed_locators import OrderFeedPageLocators as Order
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Кликнуть по заказу')
    def click_order(self):
        self.find_element(Order.ORDER).click()

    @allure.step('Получаем номер заказа')
    def get_number_order(self):
        return self.find_element(Order.ORDER_NUMBER).text

    @allure.step('Проверяем счетчик заказов "Выполнено за все время"')
    def get_counter_orders_of_all_time(self):
        return self.find_element(Order.ORDER_ALL).text

    @allure.step('Проверяем счетчик заказов "Выполнено за сегодня"')
    def get_counter_orders_for_today(self):
        return self.find_element(Order.ORDER_TODAY).text

    @allure.step('Проверяем номер заказа на странице "Лента заказов"')
    def get_order_number(self, order_number):
        element = (By.XPATH, f".//p[text()='{order_number}']")
        return self.find_element(element)
