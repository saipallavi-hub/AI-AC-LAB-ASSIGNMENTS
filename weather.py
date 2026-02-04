#write a Python program that connects to a weather API Generate code to fetch weather data securely without exposing API keys in the code.
import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')
city = input("Enter city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

response = requests.get(complete_url)
data = response.json()

if data.get("cod") == 200:
    main = data["main"]
    weather_desc = data["weather"][0]["description"]
    print(f"City: {city}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Weather: {weather_desc}")
else:
    print("Error:", data.get("message", "City Not Found"))

# Ensure to create a .env file with the line: WEATHER_API_KEY=your_api_key_here






