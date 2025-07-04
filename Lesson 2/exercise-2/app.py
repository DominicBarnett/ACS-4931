# Exercise 2: Flask Weather Application
# This application demonstrates API integration with OpenWeatherMap and potential debugging challenges
# including environment variable handling, API responses, and data processing.
#
# Key Features:
# - Uses Flask for web interface
# - Integrates with OpenWeatherMap API for weather data
# - Demonstrates use of environment variables for API keys
# - Handles and displays API responses with error handling

import os
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file


################################################
## SETUP - Application Configuration
################################################

# Initialize Flask application
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
# Get API key from environment variables for OpenWeatherMap API
API_KEY = os.getenv('API_KEY')


################################################
## ROUTES - Application Endpoints
################################################

@app.route('/')
def home():
    """Displays the homepage with forms for current or historical data."""
    # Create context with date range for historical data (last 5 days to today)
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),  # 5 days ago
        'max_date': datetime.now()  # Today
    }
    return render_template('home.html', **context)

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units.
    
    Args:
        units (str): The units system ('imperial', 'metric', or 'kelvin')
    
    Returns:
        str: Single letter representation ('F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin)
    """
    return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'

@app.route('/results')
def results():
    """Displays results for current weather conditions.
    
    This endpoint fetches weather data from OpenWeatherMap API and displays it.
    Potential debugging points:
    - API key validation
    - City name validation
    - API response structure
    - Error handling for failed requests
    """
    # Get parameters from URL query string
    city = request.args.get('city')
    units = request.args.get('units')

    # OpenWeatherMap API endpoint for current weather
    url = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Parameters for the API request
    params = {
        'appid': API_KEY,  # API key for authentication
        'q': city,         # City name to get weather for
        'units': units     # Units system (imperial, metric, or kelvin)
    }
    
    # Make API request and parse JSON response
    result_json = requests.get(url, params=params).json()
    
    # Debug print to inspect API response structure
    print("Result JSON:", result_json)

    # Extract relevant weather data from API response
    context = {
        'date': datetime.now(),                                    # Current date/time
        'city': result_json['name'],                              # City name from API
        'description': result_json['weather'][0]['description'],  # Weather description
        'temp': result_json['main']['temp'],                      # Temperature
        'humidity': result_json['main']['humidity'],              # Humidity percentage
        'wind_speed': result_json['wind']['speed'],               # Wind speed
        'units_letter': get_letter_for_units(units)               # Temperature unit letter
    }

    return render_template('results.html', **context)


# Run the application
if __name__ == '__main__':
    app.run()
