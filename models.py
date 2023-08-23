from pydantic import BaseModel

from pydantic import BaseModel

class CO2CalculationInput(BaseModel):
    event_name: str
    event_duration: int
    country: str
    participants: int
    employees: int
    heated_area: int
    air_conditioned_area: int
    number_of_people_arriving_by_car: int
    average_distance_traveled_by_car: str
    number_of_people_traveling_by_public_transport: int
    short_haul_flights: int
    medium_haul_flights: int
    long_haul_flights: int
    percentage_business_class: str
    over_night_stay_three_stars: str
    over_night_stay_four_stars: str
    over_night_stay_five_stars: str
    meal_meat_amount: str
    meal_vegetarian_amount: str
    snacks_amount: str
    soda_liters: str
    coffee_cups: str
    tea_cups: str
    wine_liters: str
    beer_liters: str
    spirits_liters: str
    power_consumption: str
    printed_matter: str
    plastics: str
    recyclable_material: str
    plant_based_materials: str
    event_stand_area: str
    transported_weight: str
    transported_distance: str
    garbage: str
    recycling: str
