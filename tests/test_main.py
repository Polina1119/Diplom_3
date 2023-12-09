from locators.main_page_locators import MainPageLocators as Main
from pages.main_page import MainPage
from pages.base_page import BasePage


class TestMain:
    def test_click_on_constructor(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        main_page.click_on_constructor()
        base_page.find_element(Main.COLLECT_BURGER)

        assert base_page.find_element(Main.COLLECT_BURGER).text == 'Соберите бургер'

    def test_click_on_order_feed(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        main_page.click_on_order_feed()

        assert base_page.find_element(Main.ORDER_FEED).text == 'Лента Заказов'

    def test_click_on_ingredient(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        main_page.scroll()
        main_page.click_on_ingredient()

        assert base_page.find_element(Main.DETAILS_INGREDIENT).text == 'Детали ингредиента'

    def test_close_window_details(self, driver):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        main_page.scroll()
        main_page.click_on_ingredient()
        main_page.close_window_with_details()

        assert base_page.find_element(Main.COLLECT_BURGER).text == 'Соберите бургер'

    def test_create_order(self, driver, login):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        main_page.click_on_constructor()
        main_page.move_ingredient_in_order(locator_1=Main.FLUORESCENT_BUN, locator_2=Main.DRAG_HERE)
        main_page.click_on_place_order()

        assert base_page.find_element(Main.ORDER_IS_PROCESSED).text == "Ваш заказ начали готовить"

    def test_counter_ingredients(self, driver, login):
        main_page = MainPage(driver)
        counter_1 = main_page.check_counter_ingredients()
        main_page.drag_and_drop_on_element(locator_1=Main.FLUORESCENT_BUN, locator_2=Main.DRAG_HERE)
        counter_2 = main_page.check_counter_ingredients()

        assert counter_1 < counter_2



















