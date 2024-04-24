import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("browser_reg")
def test_redirect_to_constructor_blocks(browser_reg):

    browser_reg.find_element(By.XPATH, textbox_name_registration_form_xpath).send_keys("Irina")
    browser_reg.find_element(By.XPATH, textbox_email_registration_form_xpath).send_keys("irina2@gmail.com")
    browser_reg.find_element(By.XPATH, textbox_password_registration_form_xpath).send_keys("Q1w2e3r4t5")
    browser_reg.find_element(By.XPATH, registration_button_xpath).click()

    WebDriverWait(browser_reg,5).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))