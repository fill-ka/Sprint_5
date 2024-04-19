from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

driver.find_element(By.NAME, "name").send_keys("anna_komova_7_251@gmail.com")
driver.find_element(By.NAME, "Пароль").send_keys("Q1w2e3r4t5")
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

driver.quit()