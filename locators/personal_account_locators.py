from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    RECOVERY_PASSWORD = (By.XPATH, '//a[contains(text(),"Восстановить пароль")]')  # кнопка Восстановить пароль
    RECOVERY_BUTTON = (By.XPATH, '//button[contains(text(),"Восстановить")]') # кнопка Восстановить
    LOOK_BUTTON = (By.CLASS_NAME, 'input__icon input__icon-action') # кнопка просмотра пароля
    EXIT = (By.XPATH, '//button[contains(text(),"Выход")]') # кнопка Выход
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')  # кнопка Войти
    EMAIL = (By.TAG_NAME, 'input')  # поле ввода email
    PASSWORD = (By.NAME, 'Пароль')  # поле ввода пароля
    ORDER_NUMBER = (By.XPATH, '//p[contains(@class, "text text_type_digits")]')  # номер заказа
    ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]')  # кнопка "Лента заказов"
    ORDERS_HISTORY = (By.XPATH, '//a[@href="/account/order-history"]')  # кнопка История заказов



