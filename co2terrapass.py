from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService

import time


service = ChromeService()
driver = webdriver.Chrome(service=service)

# Open the desired URL
driver.get('https://terrapass.com/carbon-footprint-calculator/')

button = driver.find_element(By.XPATH,'/html/body/tpc-root/tpc-home/div/div/p[4]/a')
button.click()

time.sleep(10)