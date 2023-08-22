from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = ChromeService()
driver = webdriver.Chrome(service=service)

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


# Construct the JavaScript code to find the button element
button_js = "return document.querySelector('div[class=\"carousel-item active\"] a[role=\"button\"]')"

# Execute the JavaScript code to find the button element
button = driver.execute_script(button_js)

# Click on the button element
button.click()

# Finding the input element for number of people arriving by car by ID
people_arriving_by_car = driver.find_element(
    By.ID, 'event_calculator_car_number_of_visitors')

# Sending keys to the input field to set the number of people arriving by car
people_arriving_by_car.send_keys('51900')


average_distance_traveled_car = driver.find_element(
    By.ID, 'event_calculator_car_average_distance_km')
average_distance_traveled_car.send_keys('30')


# Finding the input element for number of people traveling by public transport by ID
people_traveling_by_public_trasport = driver.find_element(
    By.ID, 'event_calculator_bus_or_train_number_of_visitors')

# Sending keys to the input field to set the number of people traveling by public transport
people_traveling_by_public_trasport.send_keys('80000')

# Finding the input element for average distance traveled by car by ID
average_distance_traveled_public = driver.find_element(
    By.ID, 'event_calculator_bus_or_train_average_distance_km')

# Sending keys to the input field to set the average distance traveled by car
average_distance_traveled_public.send_keys('40')

# Finding the input element for short-haul flights by ID
short_hault_flights = driver.find_element(
    By.ID, 'event_calculator_short_flights_amount')

# Sending keys to the input field to set the number of short-haul flights
short_hault_flights.send_keys('500')

medium_haul_flights = driver.find_element(
    By.ID, 'event_calculator_medium_flights_amount')

medium_haul_flights.send_keys('30')

long_flights_amount_input = driver.find_element(
    By.ID, 'event_calculator_long_flights_amount')
long_flights_amount_input.send_keys('5')


percentage_bussines_class = driver.find_element(
    By.ID, 'event_calculator_business_or_first_flights_per_cent')
percentage_bussines_class.send_keys('5')

button_2 = driver.find_element(
    By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
button_2.click()


over_night_stay_three_stars = driver.find_element(
    By.ID, 'event_calculator_stay_number_3_stars')
# Replace '10' with your desired value
over_night_stay_three_stars.send_keys('10')

# Similar code for the other input fields (4-star and 5-star hotels)
over_night_stay_four_stars = driver.find_element(
    By.ID, 'event_calculator_stay_number_4_stars')
# Replace '5' with your desired value
over_night_stay_four_stars.send_keys('5')

over_night_stay_five_stars = driver.find_element(
    By.ID, 'event_calculator_stay_number_5_stars')
# Replace '3' with your desired value
over_night_stay_five_stars.send_keys('3')


button_3 = driver.find_element(
    By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
button_3.click()


meal_meat_amount = driver.find_element(
    By.ID, 'event_calculator_warm_meal_meat_amount')
meal_meat_amount.send_keys('50')  # Replace '50' with your desired value

meal_vegetarian_amount = driver.find_element(
    By.ID, 'event_calculator_warm_meal_vegetarian_amount')
meal_vegetarian_amount.send_keys('30')  # Replace '30' with your desired value

snacks_amount = driver.find_element(By.ID, 'event_calculator_snacks')
snacks_amount.send_keys('100')  # Replace '100' with your desired value

soda_liters = driver.find_element(By.ID, 'event_calculator_soda_liters')
soda_liters.send_keys('200')  # Replace '20' with your desired value

coffee_cups = driver.find_element(By.ID, 'event_calculator_coffee_portions')
coffee_cups.send_keys('100')  # Replace '100' with your desired value

tea_cups = driver.find_element(By.ID, 'event_calculator_tea_portions')
tea_cups.send_keys('80')  # Replace '80' with your desired value

wine_liters = driver.find_element(By.ID, 'event_calculator_wine_liters')
wine_liters.send_keys('15.5')  # Replace '15.5' with your desired value

beer_liters = driver.find_element(By.ID, 'event_calculator_beer_liters')
beer_liters.send_keys('30')  # Replace '30' with your desired value

# Spirits Liters
spirits_liters = driver.find_element(
    By.ID, 'event_calculator_spirits_liters')
# Replace '10.2' with your desired value
spirits_liters.send_keys('10.2')

button_4 = driver.find_element(
    By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
button_4.click()


# Power Consumption
power_consumption = driver.find_element(
    By.ID, 'event_calculator_power_consumption_kwh')
# Replace '150' with your desired value
power_consumption.send_keys('1500')

button_5 = driver.find_element(
    By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
button_5.click()
# Printed Matter
printed_matters = driver.find_element(
    By.ID, 'event_calculator_printed_matters_kg')
printed_matters.send_keys('10.5')  # Replace with the desired value

# Synthetic Materials
plastics = driver.find_element(
    By.ID, 'event_calculator_synthetic_materials')
plastics.send_keys('200')  # Replace with the desired value

# Recyclable Products
recyclable_material = driver.find_element(
    By.ID, 'event_calculator_recyclable_products')
recyclable_material.send_keys('100')  # Replace with the desired value

# Vegetable Products
plant_based_materials = driver.find_element(
    By.ID, 'event_calculator_vegetable_products')
plant_based_materials.send_keys('100')  # Replace with the desired value

# Area of the Stand
event_stand_area = driver.find_element(
    By.ID, 'event_calculator_event_stand_area')
event_stand_area.send_keys('50.0')  # Replace with the desired value

button_6 = driver.find_element(
    By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
button_6.click()

# Transported Weight
transported_weight = driver.find_element(
    By.ID, 'event_calculator_transported_weight')
# Replace '3.5' with your desired value
transported_weight.send_keys('12000')

# Transported Distance
transported_distance = driver.find_element(
    By.ID, 'event_calculator_transported_distance')
# Replace '120' with your desired value
transported_distance.send_keys('120')

# Residual Waste
garbage = driver.find_element(By.ID, 'event_calculator_garbage_kg')
garbage.send_keys('1000')  # Replace '50' with your desired value

# Recycling Waste
recycling = driver.find_element(
    By.ID, 'event_calculator_garbage_recycling_kg')
# Replace '20' with your desired value
recycling.send_keys('200')

# Find the form element with ID 'new_event_calculator'
form_element = driver.find_element(By.ID, 'new_event_calculator')
# Submit the form
form_element.submit()

wait = WebDriverWait(driver, 5)

# Wait for the CO2 amount details to be displayed
co2_amount_element = wait.until(
    EC.presence_of_element_located((By.ID, 'co2_amount'))
)

# Extract the CO2 amount from the text (removing unnecessary characters and spaces)
co2_amount_text = co2_amount_element.text
co2_amount = co2_amount_text.replace(
    'CO2 amount:', '').replace('t', '').replace(',', '').strip()

# Log the CO2 amount to the console
print(f"CO2 Amount: {co2_amount} t")

# Locate and wait for the alert section to be displayed
alert_section = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'alert-gray'))
)

# Extract data from the alert section
sections = alert_section.find_elements(By.CLASS_NAME, 'js-highlight-section')

# Loop through the sections and extract data
for section in sections:
    section_name = section.find_element(By.TAG_NAME, 'dt').text
    section_amount = section.find_element(By.TAG_NAME, 'dd').text
    print(f"{section_name}: {section_amount}")

# Pause execution for a while
time.sleep(100)
