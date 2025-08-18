from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Colombo") :
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    wheather_data = requests.get(request_url).json()

    return wheather_data

if __name__ == "__main__" :
    print("\n***Get Current Wheather Condition***\n")
    city = input("\nPlease enter a city name: ")
    if not bool(city.strip()) :
        city = "Colombo"
    

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)