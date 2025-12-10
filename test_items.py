import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button is not None
