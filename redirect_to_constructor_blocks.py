from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

driver.find_element(By.NAME, "name").send_keys("anna_komova_7_251@gmail.com")
driver.find_element(By.NAME, "Пароль").send_keys("Q1w2e3r4t5")
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
element = driver.find_element(By.XPATH, ".//p[text()='Сыр с астероидной плесенью']")
driver.execute_script("arguments[0].scrollIntoView();", element)

driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
driver.find_element(By.XPATH, ".//p[text()='Соус Spicy-X']")

driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
driver.find_element(By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")

driver.quit()