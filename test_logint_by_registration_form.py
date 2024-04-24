import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("browser_reg")
def test_redirect_to_constructor_blocks(browser_reg):

    browser_reg.find_element(By.XPATH, login_button_registration_form).click()

    WebDriverWait(browser_reg,5).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))

    browser_reg.find_element(By.XPATH, textbox_email_xpath).send_keys("anna_komova_7_251@gmail.com")
    browser_reg.find_element(By.XPATH, textbox_password_xpath).send_keys("Q1w2e3r4t5")
    browser_reg.find_element(By.XPATH, login_button_xpath).click()

    WebDriverWait(browser_reg,5).until(EC.visibility_of_element_located((By.XPATH, create_order_button_xpath)))