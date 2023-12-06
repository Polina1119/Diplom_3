import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://stellarburgers.nomoreparties.site/'

    @allure.step('Открываем страницу StellarBurgers')
    def go_to_site(self):
        return self.driver.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not find {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not find {locator}')

    def execute_script(self, locator):
        return self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def current_url(self):
        return self.driver.current_url

    def drag_and_drop_on_element(self, locator_1, locator_2):
        draggable = self.find_element(locator_1)
        droppable = self.find_element(locator_2)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

