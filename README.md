# weather-app-python
app

A simple command-line weather application that provides current weather information for any city worldwide.

## Features

- Get real-time weather data for any city
- View current temperature, "feels like" temperature, and weather conditions
- See humidity levels and wind speed
- Display sunrise and sunset times
- Clean, formatted output in the terminal

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/weather-app-python.git
   cd weather-app-python
   ```

2. Install required dependencies:
   ```
   pip install requests
   ```

3. Get an API key:
   - Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/)
   - Create an account and navigate to the API keys section

## Usage

### Setting Up Your API Key

Option 1: Set as environment variable (recommended):
```
# Windows Command Prompt
set OPENWEATHER_API_KEY=your_api_key_here

# Windows PowerShell
$env:OPENWEATHER_API_KEY="your_api_key_here"

# macOS/Linux
export OPENWEATHER_API_KEY=your_api_key_here
```

Option 2: Replace directly in the code (less secure):
Replace `"your_api_key_here"` in the `get_weather` function with your actual API key.

### Running the Application

```
python weather_app.py
```

Follow the on-screen prompts to check weather for your desired city.

## Example Output

```
=== Python Weather App ===

Options:
1. Get weather by city name
2. Exit
Enter your choice (1-2): 1
Enter city name: London

Fetching weather data...

Weather in London, GB:
-----------------------------
Condition: Partly cloudy
Temperature: 14.2°C
Feels like: 13.6°C
Humidity: 78%
Wind speed: 5.2 m/s
Sunrise: 06:32
Sunset: 19:48
-----------------------------
Last updated: 2025-04-16 15:23:45
```

## How It Works

The application uses the OpenWeatherMap API to fetch current weather data. It sends an HTTP request with your city query and API key, then receives and formats the JSON response into readable weather information.

## Future Improvements

- Add support for weather forecasts
- Implement location detection
- Add temperature unit conversion option
- Create a graphical user interface

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
