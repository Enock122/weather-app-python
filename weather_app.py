import requests
import json
import os
from datetime import datetime

def get_weather(city):
    """
    Fetch weather data for a given city using the OpenWeatherMap API
    """
    # You'll need to sign up for a free API key at https://openweathermap.org/
    api_key = os.environ.get("OPENWEATHER_API_KEY", "419ca40f0d85115ddf1522b521e87ae0")
    
    # Base URL for OpenWeatherMap API
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units (Celsius)
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return format_weather_data(data)
        else:
            return f"Error: Unable to fetch weather data. Status code: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def format_weather_data(data):
    """
    Format the raw weather data into a readable format
    """
    # Extract relevant information
    city_name = data["name"]
    country = data["sys"]["country"]
    weather_desc = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
    sunset_time = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
    
    # Format the weather information
    weather_info = f"""
Weather in {city_name}, {country}:
-----------------------------
Condition: {weather_desc}
Temperature: {temp}°C
Feels like: {feels_like}°C
Humidity: {humidity}%
Wind speed: {wind_speed} m/s
Sunrise: {sunrise_time}
Sunset: {sunset_time}
-----------------------------
Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
    return weather_info

def main():
    """
    Main function to run the weather app
    """
    print("=== Python Weather App ===")
    
    while True:
        print("\nOptions:")
        print("1. Get weather by city name")
        print("2. Exit")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == "1":
            city = input("Enter city name: ")
            print("\nFetching weather data...")
            weather_info = get_weather(city)
            print(weather_info)
        elif choice == "2":
            print("Thank you for using the Weather App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
