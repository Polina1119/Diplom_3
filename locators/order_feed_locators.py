from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER = (By.XPATH, '//li[contains(@class, "OrderHistory")]') # заказ в ленте
    DETAILS_ORDER = (By.XPATH, '//p[contains(text(),"Cостав")]') # детали заказа
    ORDER_ALL = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]') # заказы за все время
    ORDER_TODAY = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')  # заказы за сегодня
    IN_WORK = (By.CLASS_NAME, 'text text_type_digits-default mb-2') # заказ в работе
    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')  # номер заказа
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # кнопка "Лента заказов"