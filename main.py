from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

import time

# Start the Chrome browser
driver = webdriver.Chrome()

# Open the desired URL
driver.get("https://co2.myclimate.org/en/event_calculators/new")  # Replace with the actual URL

time.sleep(10)
try:
# Find and click the accept all button for cookies
    element = driver.execute_script("""return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
    element.click()
except:
    pass
# Finding the input element for event name by ID
event_name = driver.find_element(By.ID, "event_calculator_name")

# Sending keys to the input field to set the event name
event_name.send_keys("Estereo Picnic")  # Replace "Your Desired Input" with the text you want to input

# Finding the input element for event duration by ID
event_duration = driver.find_element(By.ID, "event_calculator_event_duration_in_days")

# Sending keys to the input field to set the event duration
event_duration.send_keys("4")

# Finding the select element for country by ID
select_country = driver.find_element(By.ID, "event_calculator_country")

# Selecting a country from the dropdown
country = Select(select_country).select_by_visible_text('Germany')

# Finding the input element for number of participants by ID
number_participants = driver.find_element(By.ID, "event_calculator_number_of_participants")

# Sending keys to the input field to set the number of participants
number_participants.send_keys('10000')



number_employees = driver.find_element(By.ID,'event_calculator_number_of_employees') 

number_employees.send_keys('200')


heated_area = driver.find_element(By.ID,'event_calculator_heated_square_meters')

heated_area.send_keys('10000')

air_conditioned_area = driver.find_element(By.ID,'event_calculator_air_cond_square_meters')

air_conditioned_area.send_keys('10000')
# Find all the <a> elements on the page



# Wait for a moment to ensure data is processed
time.sleep(5)

# Close the browser
driver.quit()

 