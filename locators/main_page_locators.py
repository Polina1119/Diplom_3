from selenium.webdriver.common.by import By


class MainPageLocators:
    LK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')  # кнопка Личный кабинет
    CONSTRUCTOR = (By.XPATH, '//p[contains(text(),"Конструктор")]')  # кнопка Конструктор
    ORDER_FEED = (By.XPATH, '//p[contains(text(),"Лента Заказов")]') # кнопка Лента заказов
    FLUORESCENT_BUN = (By.XPATH, '(//img[@alt="Флюоресцентная булка R2-D3"])')  # Флюоресцентная булка R2-D3
    DETAILS_INGREDIENT = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]') # заголовок Детали ингредиента
    CLOSE = (By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS') # крестик
    PLACE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]') # кнопка "Оформить заказ"
    ID_ORDER = (By.XPATH, '//p[contains(text(),"идентификатор заказа")]') # идентификатор заказа
    ORDER_NUMBER = (By.TAG_NAME, 'h2') # номер заказа
    COLLECT_BURGER = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]') # заголовок Соберите бургер
    COUNTER_INGREDIENTS = (By.XPATH, '//p[contains(@class, "counter_counter__num")]')  # счетчик ингредиентов
    ORDER_IS_PROCESSED = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]') # заголовок "Ваш заказ начали готовить"
    DRAG_HERE = (By.XPATH, '//ul[contains(@class, "BurgerConstructor")]')  # перетащить ингредиент


    


