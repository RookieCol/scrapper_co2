from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

# Start the Chrome browser
driver = webdriver.Chrome()

# Open the desired URL
driver.get("https://co2.myclimate.org/en/event_calculators/new")  # Replace with the actual URL

# Wait for the "Accept cookies" button to be clickable
try:
    
    shadow_root = driver.find_element(By.CSS_SELECTOR, "#usercentrics-root").shadow_root
    shadow_root.find_element(By.CSS_SELECTOR, "button[data-testid='uc-accept-all-button']").click()
except:
    pass

#fill form 
name_input = driver.find_element(By.ID, "event_calculator_name")
name_input.send_keys("Your Name") 




time.sleep(5)
driver.quit()
