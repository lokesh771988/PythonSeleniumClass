import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.mceapps.com/")

driver.find_element(By.CLASS_NAME, "my_show").click()
time.sleep(10)
