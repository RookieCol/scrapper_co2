# CO2 MyClimate Calculator

This is a FastAPI-based web application that calculates CO2 emissions for events using the MyClimate calculator.

## Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

- [Ngrok](https://ngrok.com/)

### Installation

1. Install the needed modules
```
pip install -r requirements.txt
```
2. start the server
```
uvicorn co2myclimate:app --host 0.0.0.0 --port 8000 --reload  
```
3. Expose it using ngrok 
```
ngrok http 8000
```