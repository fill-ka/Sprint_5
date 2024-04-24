import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("browser")
def test_redirect_to_constructor_blocks(browser):
    browser.find_element(By.XPATH, login_in_account_button_xpath).click()

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))

    browser.find_element(By.XPATH, textbox_email_xpath).send_keys("anna_komova_7_251@gmail.com")
    browser.find_element(By.XPATH, textbox_password_xpath).send_keys("Q1w2e3r4t5")
    browser.find_element(By.XPATH, login_button_xpath).click()

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, create_order_button_xpath)))

    browser.find_element(By.XPATH, LK_header_xpath).click()

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, save_button_in_LK_xpath)))