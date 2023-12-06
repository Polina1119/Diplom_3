import allure
from locators.order_feed_locators import OrderFeedPageLocators as Order
from locators.main_page_locators import MainPageLocators as Main
from pages.personal_account_page import PersonalAccountPage as LK
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    @allure.title('При клике на заказ появляется модальное окно с деталями заказа')
    def test_order_details(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_order_feed()
        order_feed_page.click_order()

        assert main_page.find_element(Order.DETAILS_ORDER).text == 'Состав'

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_details_displayed_in_orders_feed(self, driver, login):
        main_page = MainPage(driver)
        main_page.check_counter_ingredients()
        main_page.drag_and_drop_on_element(locator_1=Main.FLUORESCENT_BUN, locator_2=Main.DRAG_HERE)
        main_page.click_on_place_order()
        main_page.close_window()
        main_page.click_on_lk()
        lk = LK(driver)
        lk.click_button_history_orders()
        order_number = lk.get_order_number()
        lk.click_button_history_orders()
        order_feed_page = OrderFeedPage(driver)

        assert order_feed_page.check_order_number(order_number)

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_after_create_order_counter_orders_of_all_time_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        counter_1 = order_feed_page.check_counter_orders_of_all_time()
        main_page.click_on_constructor()
        main_page.drag_and_drop_on_element(locator_1=Main.FLUORESCENT_BUN, locator_2=Main.DRAG_HERE)
        main_page.click_on_place_order()
        main_page.close_window()
        main_page.click_on_order_feed()
        counter_2 = order_feed_page.check_counter_orders_of_all_time()

        assert int(counter_1) < int(counter_2)

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_after_create_order_counter_orders_for_today_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        counter_1 = order_feed_page.check_counter_orders_for_today()
        main_page.click_on_constructor()
        main_page.drag_and_drop_on_element(locator_1=Main.FLUORESCENT_BUN, locator_2=Main.DRAG_HERE)
        main_page.click_on_place_order()
        main_page.close_window()
        main_page.click_on_order_feed()
        counter_2 = order_feed_page.check_counter_orders_for_today()

        assert int(counter_1) < int(counter_2)

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_after_create_order_number_order_to_in_work(self, driver, login):
        main_page = MainPage(driver)
        main_page.check_counter_ingredients()
        main_page.drag_and_drop_on_element(locator_1=Main.FLUORESCENT_BUN, locator_2=Main.DRAG_HERE)
        main_page.click_on_place_order()
        order_number = main_page.check_order_number()
        main_page.close_window()
        main_page.click_on_order_feed()

        assert str(order_number) in main_page.find_element(Order.IN_WORK).text
