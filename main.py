from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Start the Chrome browser with options
options = Options()
options.page_load_strategy = 'eager'
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Open the desired URL
driver.get("https://co2.myclimate.org/en/event_calculators/new")

# Function to check if the button is clickable
def is_button_clickable():
    try:
        element = driver.execute_script(
            """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
        return element.is_displayed() and element.is_enabled()
    except:
        return False

# Keep looping until the button is clickable
while not is_button_clickable():
    time.sleep(1)  # Wait for 1 second before checking again

# Click the accept button for cookies
element = driver.execute_script(
    """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
element.click()

# Set implicit wait time
driver.implicitly_wait(20)
# Finding the input element for event name by ID
event_name = driver.find_element(By.ID, "event_calculator_name")

# Sending keys to the input field to set the event name
event_name.send_keys("Estereo Picnic")

# Finding the input element for event duration by ID
event_duration = driver.find_element(
    By.ID, "event_calculator_event_duration_in_days")

# Sending keys to the input field to set the event duration
event_duration.send_keys("4")

# Finding the select element for country by ID
select_country = driver.find_element(By.ID, "event_calculator_country")

# Selecting a country from the dropdown
country = Select(select_country).select_by_visible_text('Colombia')

# Finding the input element for number of participants by ID
number_participants = driver.find_element(
    By.ID, "event_calculator_number_of_participants")

# Sending keys to the input field to set the number of participants
number_participants.send_keys('173000')

# Finding the input element for number of employees by ID
number_employees = driver.find_element(
    By.ID, 'event_calculator_number_of_employees')

# Sending keys to the input field to set the number of employees
number_employees.send_keys('200')

# Finding the input element for heated area by ID
heated_area = driver.find_element(
    By.ID, 'event_calculator_heated_square_meters')

# Sending keys to the input field to set the heated area
heated_area.send_keys('0')

# Finding the input element for air conditioned area by ID
air_conditioned_area = driver.find_element(
    By.ID, 'event_calculator_air_cond_square_meters')

# Sending keys to the input field to set the air conditioned area
air_conditioned_area.send_keys('500')

# Finding the input element for number of people arriving by car by ID
people_arriving_by_car = driver.find_element(
    By.ID,'event_calculator_car_number_of_visitors')

# Sending keys to the input field to set the number of people arriving by car
people_arriving_by_car.send_keys('51900')

average_distance_traveled_car = driver.find_element(By.ID,'event_calculator_car_average_distance_km')
average_distance_traveled_car.send_keys('30')


# Finding the input element for number of people traveling by public transport by ID
people_traveling_by_public_trasport = driver.find_element(
    By.ID,'event_calculator_bus_or_train_number_of_visitors')

# Sending keys to the input field to set the number of people traveling by public transport
people_traveling_by_public_trasport.send_keys('80000')

# Finding the input element for average distance traveled by car by ID
average_distance_traveled_public = driver.find_element(
    By.ID,'event_calculator_bus_or_train_average_distance_km')

# Sending keys to the input field to set the average distance traveled by car
average_distance_traveled_public.send_keys('40')

# Finding the input element for short-haul flights by ID
short_hault_flights = driver.find_element(By.ID,'event_calculator_short_flights_amount')

# Sending keys to the input field to set the number of short-haul flights
short_hault_flights.send_keys('500')

medium_haul_flights = driver.find_element(By.ID,'event_calculator_medium_flights_amount')

medium_haul_flights.send_keys('30')

long_flights_amount_input = driver.find_element(By.ID, 'event_calculator_long_flights_amount')
long_flights_amount_input.send_keys('5')


percentage_bussines_class = driver.find_element(By.ID,'event_calculator_business_or_first_flights_per_cent')
percentage_bussines_class.send_keys('5')

