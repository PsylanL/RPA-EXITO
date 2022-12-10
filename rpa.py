from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()
time.sleep(1)
driver.get("https://www.mercadolibre.com.co/#from=homecom")



driver.quit()