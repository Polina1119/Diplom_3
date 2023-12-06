from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:
    PASSWORD_RECOVERY_TEXT = (By.XPATH, '//h2[text()="Восстановление пароля"]')  # Восстановление пароля
    EMAIL = (By.XPATH, '//input[contains(@class, "text")]')  # Email
    SAVE = (By.XPATH, '//button[contains(text(),"Сохранить")]') # кнопка Сохранить
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка Восстановить
    SEE_PASSWORD = (By.XPATH, '//div[contains(@class, "input__icon")]')  # кнопка показать/скрыть пароль
    ACTIVE_PASSWORD = (By.XPATH, '//div[contains(@class, "input_status_active")]')
