import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

@pytest.mark.usefixtures("browser_rec_pas")
def test_redirect_to_constructor_blocks(browser_rec_pas):

    browser_rec_pas.find_element(By.XPATH, login_button_recovery_password_form_xpath).click()

    WebDriverWait(browser_rec_pas,5).until(EC.visibility_of_element_located((By.XPATH, login_button_xpath)))

    browser_rec_pas.find_element(By.XPATH, textbox_email_xpath).send_keys("anna_komova_7_251@gmail.com")
    browser_rec_pas.find_element(By.XPATH, textbox_password_xpath).send_keys("Q1w2e3r4t5")
    browser_rec_pas.find_element(By.XPATH, login_button_xpath).click()

    WebDriverWait(browser_rec_pas,5).until(EC.visibility_of_element_located((By.XPATH, create_order_button_xpath)))