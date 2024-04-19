from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("Olga")
driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys("olga@gmail.com")
driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys("12345")
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))

driver.quit()