from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from models import CO2CalculationInput  # Adjust the import path based on your project structure
import time

app = FastAPI()

def wait_for_button_to_be_clickable(driver, button_locator):
    return WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(button_locator)
    )

def is_button_clickable(driver):
    try:
        element = driver.execute_script(
            """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
        return element.is_displayed() and element.is_enabled()
    except:
        return False

@app.post('/co2calculation')
def calculate_co2(input_data: CO2CalculationInput):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    service = ChromeService()
    driver = webdriver.Chrome(service=service,options=options)

    try:
        # Open the desired URL
        driver.get("https://co2.myclimate.org/en/event_calculators/new")

        while not is_button_clickable(driver):
            time.sleep(1)

        element = driver.execute_script(
            """return document.querySelector('#usercentrics-root').shadowRoot.querySelector("button[data-testid='uc-accept-all-button']")""")
        element.click()

        # Fill out the form using input_data from the request
        event_name = driver.find_element(By.ID, "event_calculator_name")
        event_name.send_keys(input_data.event_name)
        # Finding the input element for event duration by ID
        event_duration = driver.find_element(
            By.ID, "event_calculator_event_duration_in_days")

        # Sending keys to the input field to set the event duration
        event_duration.send_keys(input_data.event_duration)

        # Finding the select element for country by ID
        select_country = driver.find_element(By.ID, "event_calculator_country")

        # Selecting a country from the dropdown
        country = Select(select_country).select_by_visible_text(input_data.country)

        # Finding the input element for number of participants by ID
        number_participants = driver.find_element(
        By.ID, "event_calculator_number_of_participants")

        # Sending keys to the input field to set the number of participants
        number_participants.send_keys('173000')

        # Finding the input element for number of employees by ID
        number_employees = driver.find_element(
        By.ID, 'event_calculator_number_of_employees')

        # Sending keys to the input field to set the number of employees
        number_employees.send_keys(input_data.employees)

        # Finding the input element for heated area by ID
        heated_area = driver.find_element(
            By.ID, 'event_calculator_heated_square_meters')

                # Sending keys to the input field to set the heated area
        heated_area.send_keys(input_data.heated_area)

        # Finding the input element for air conditioned area by ID
        air_conditioned_area = driver.find_element(
            By.ID, 'event_calculator_air_cond_square_meters')

        # Sending keys to the input field to set the air conditioned area
        air_conditioned_area.send_keys(input_data.air_conditioned_area)


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
        people_arriving_by_car.send_keys(input_data.number_of_people_arriving_by_car)


        average_distance_traveled_car = driver.find_element(
            By.ID, 'event_calculator_car_average_distance_km')
        average_distance_traveled_car.send_keys(input_data.average_distance_traveled_by_car)


        # Finding the input element for number of people traveling by public transport by ID
        people_traveling_by_public_trasport = driver.find_element(
            By.ID, 'event_calculator_bus_or_train_number_of_visitors')

        # Sending keys to the input field to set the number of people traveling by public transport
        people_traveling_by_public_trasport.send_keys(input_data.number_of_people_traveling_by_public_transport)

        # Finding the input element for average distance traveled by car by ID
        average_distance_traveled_public = driver.find_element(
            By.ID, 'event_calculator_bus_or_train_average_distance_km')

        # Sending keys to the input field to set the average distance traveled by car
        average_distance_traveled_public.send_keys(input_data.average_distance_traveled_by_car)

        # Finding the input element for short-haul flights by ID
        short_hault_flights = driver.find_element(
            By.ID, 'event_calculator_short_flights_amount')

        # Sending keys to the input field to set the number of short-haul flights
        short_hault_flights.send_keys(input_data.short_haul_flights)

        medium_haul_flights = driver.find_element(
            By.ID, 'event_calculator_medium_flights_amount')

        medium_haul_flights.send_keys(input_data.medium_haul_flights)

        long_flights_amount_input = driver.find_element(
            By.ID, 'event_calculator_long_flights_amount')
        long_flights_amount_input.send_keys(input_data.long_haul_flights)


        percentage_bussines_class = driver.find_element(
            By.ID, 'event_calculator_business_or_first_flights_per_cent')
        percentage_bussines_class.send_keys(input_data.percentage_business_class)
        
        

        button_2_locator = (By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
        wait_for_button_to_be_clickable(driver, button_2_locator).click()


        over_night_stay_three_stars = driver.find_element(
            By.ID, 'event_calculator_stay_number_3_stars')
        # Replace '10' with your desired value
        over_night_stay_three_stars.send_keys(input_data.over_night_stay_three_stars)

        # Similar code for the other input fields (4-star and 5-star hotels)
        over_night_stay_four_stars = driver.find_element(
            By.ID, 'event_calculator_stay_number_4_stars')
        # Replace '5' with your desired value
        over_night_stay_four_stars.send_keys(input_data.over_night_stay_four_stars)

        over_night_stay_five_stars = driver.find_element(
            By.ID, 'event_calculator_stay_number_5_stars')
        # Replace '3' with your desired value
        over_night_stay_five_stars.send_keys(input_data.over_night_stay_five_stars)

       
        button_3_locator = (By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
        wait_for_button_to_be_clickable(driver, button_3_locator).click()



        meal_meat_amount = driver.find_element(
            By.ID, 'event_calculator_warm_meal_meat_amount')
        meal_meat_amount.send_keys(input_data.meal_meat_amount)  # Replace '50' with your desired value

        meal_vegetarian_amount = driver.find_element(
            By.ID, 'event_calculator_warm_meal_vegetarian_amount')
        meal_vegetarian_amount.send_keys(input_data.meal_vegetarian_amount)  # Replace '30' with your desired value

        snacks_amount = driver.find_element(By.ID, 'event_calculator_snacks')
        snacks_amount.send_keys(input_data.snacks_amount)  # Replace '100' with your desired value

        soda_liters = driver.find_element(By.ID, 'event_calculator_soda_liters')
        soda_liters.send_keys(input_data.soda_liters)  # Replace '20' with your desired value

        coffee_cups = driver.find_element(By.ID, 'event_calculator_coffee_portions')
        coffee_cups.send_keys(input_data.coffee_cups)  # Replace '100' with your desired value

        tea_cups = driver.find_element(By.ID, 'event_calculator_tea_portions')
        tea_cups.send_keys(input_data.tea_cups)  # Replace '80' with your desired value

        wine_liters = driver.find_element(By.ID, 'event_calculator_wine_liters')
        wine_liters.send_keys(input_data.wine_liters)  # Replace '15.5' with your desired value

        beer_liters = driver.find_element(By.ID, 'event_calculator_beer_liters')
        beer_liters.send_keys(input_data.beer_liters)  # Replace '30' with your desired value

        # Spirits Liters
        spirits_liters = driver.find_element(
            By.ID, 'event_calculator_spirits_liters')
        # Replace '10.2' with your desired value
        spirits_liters.send_keys(input_data.spirits_liters)

        
        button_4_locator = (By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
        wait_for_button_to_be_clickable(driver, button_4_locator).click()


        # Power Consumption
        power_consumption = driver.find_element(
            By.ID, 'event_calculator_power_consumption_kwh')
        # Replace '150' with your desired value
        power_consumption.send_keys(input_data.power_consumption)
        
        button_5_locator = (By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
        wait_for_button_to_be_clickable(driver, button_5_locator).click()

        # Printed Matter
        printed_matters = driver.find_element(
            By.ID, 'event_calculator_printed_matters_kg')
        printed_matters.send_keys(input_data.printed_matter)  # Replace with the desired value

        # Synthetic Materials
        plastics = driver.find_element(
            By.ID, 'event_calculator_synthetic_materials')
        plastics.send_keys(input_data.plastics)  # Replace with the desired value

        # Recyclable Products
        recyclable_material = driver.find_element(
            By.ID, 'event_calculator_recyclable_products')
        recyclable_material.send_keys(input_data.recyclable_material)  # Replace with the desired value

        # Vegetable Products
        plant_based_materials = driver.find_element(
            By.ID, 'event_calculator_vegetable_products')
        plant_based_materials.send_keys(input_data.plant_based_materials)  # Replace with the desired value

        # Area of the Stand
        event_stand_area = driver.find_element(
            By.ID, 'event_calculator_event_stand_area')
        event_stand_area.send_keys(input_data.event_stand_area)  # Replace with the desired value
        

       
        button_6_locator = (By.CSS_SELECTOR, 'div[class=\'carousel-item active\'] a:nth-child(2)')
        wait_for_button_to_be_clickable(driver, button_6_locator).click()
        # Transported Weight
        transported_weight = driver.find_element(
            By.ID, 'event_calculator_transported_weight')
        # Replace '3.5' with your desired value
        transported_weight.send_keys(input_data.transported_weight)

        # Transported Distance
        transported_distance = driver.find_element(
            By.ID, 'event_calculator_transported_distance')
        # Replace '120' with your desired value
        transported_distance.send_keys(input_data.transported_distance)

        # Residual Waste
        garbage = driver.find_element(By.ID, 'event_calculator_garbage_kg')
        garbage.send_keys(input_data.garbage)  # Replace '50' with your desired value

        # Recycling Waste
        recycling = driver.find_element(
            By.ID, 'event_calculator_garbage_recycling_kg')
        # Replace '20' with your desired value
        recycling.send_keys(input_data.recycling)

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

        # Locate and wait for the alert section to be displayed
        alert_section = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'alert-gray'))
        )
        
        # Extract data from the alert section
        sections = alert_section.find_elements(By.CLASS_NAME, 'js-highlight-section')

        # Crear un diccionario para almacenar las secciones y sus cantidades
        section_data = {}

        # Loop through the sections and extract data
        for section in sections:
            section_name = section.find_element(By.TAG_NAME, 'dt').text
            section_amount = section.find_element(By.TAG_NAME, 'dd').text
            section_data[section_name] = section_amount

       

        # Crear el diccionario de resultados
        result = {
            "co2_amount": co2_amount_text,
            "sections": section_data
        }

        # Devolver la respuesta en formato JSON
        return JSONResponse(content=result)
    

    except Exception as e:
        # Handle any errors that might occur during the process
        driver.quit()
        error_message = str(e)
        
        # Re-raise the exception to FastAPI for handling
        raise HTTPException(status_code=500, detail=f"An error occurred: {error_message}")
