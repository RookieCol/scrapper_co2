import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://co2.myclimate.org/en/event_calculators/new'
response = requests.get(url)



# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all clickable elements (links and buttons)
clickable_links = soup.find_all('a')  # Find all <a> (anchor) elements
clickable_buttons = soup.find_all('button')  # Find all <button> elements
clickable_inputs = soup.find_all('input', type=['button', 'submit'])  # Find <input> elements of type "button" or "submit"

# Combine all clickable elements into a single list
all_clickable_elements = clickable_links + clickable_buttons + clickable_inputs

# Print additional information about each clickable element
for element in all_clickable_elements:
    text = element.text.strip()
    attributes = element.attrs
    href = attributes.get('href', 'No href attribute')
    onclick = attributes.get('onclick', 'No onclick attribute')

    print("Clickable Text:", text)
    print("Attributes:", attributes)
    print("Href:", href)
    print("Onclick:", onclick)
    print("------------------------------")