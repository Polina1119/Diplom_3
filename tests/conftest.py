import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome
from selenium.webdriver.firefox.service import Service as Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from locators.main_page_locators import MainPageLocators as Main
from locators.personal_account_locators import PersonalAccountPageLocators as LK
import data


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(service=Chrome(ChromeDriverManager().install()))
    if request.param == 'firefox':
        driver = webdriver.Firefox(service=Firefox(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get(data.url)
    yield driver
    driver.quit()


@pytest.fixture
def register_user():
    payload = {
        "email": data.email,
        "password": data.password,
        "name": data.name
    }
    response = requests.post(f'{data.url}api/auth/register', data=payload)
    yield payload
    token = response.json()['accessToken']
    requests.delete(f'{data.url}api/auth/user', headers={"Authorization": token})


@pytest.fixture
def login(register_user, driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main.LK)).click()
    driver.find_element(*LK.EMAIL).send_keys(register_user.get("email"))
    driver.find_element(*LK.PASSWORD).send_keys(register_user.get("password"))
    driver.find_element(*LK.LOGIN_BUTTON).click()
    return driver
