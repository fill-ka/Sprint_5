import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def browser_rec_pas():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def browser_reg():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver
    driver.quit()