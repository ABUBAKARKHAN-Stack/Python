import requests
from typing import Dict, Any


def fetch_weather_details(city):
    WEATHER_API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=6290e52d417019e58d731344aafb0718&units=metric"
    try:
        response = requests.get(WEATHER_API_URL)
        response.raise_for_status()
        data: Dict[str, Any] = response.json()

        # City Name
        city_name = data.get("name", "N/A")

        # Main Weather Details
        main_weather_details: Dict[str, Any] = data.get("weather", [{}])[0]
        weather = main_weather_details.get("main", "N/A")
        description = main_weather_details.get("description", "N/A")

        # Main Temperature Details
        main_temp_details: Dict[str, Any] = data.get("main", {})
        temperature = main_temp_details.get("temp", "N/A")
        feels_like_temp = main_temp_details.get("feels_like", "N/A")
        humidity = main_temp_details.get("humidity", "N/A")

        # Wind Details
        wind_details: Dict[str, Any] = data.get("wind", {})
        wind_speed = wind_details.get("speed", "N/A")
        wind_angle = wind_details.get("deg", "N/A")

        # Print details
        print(f"\nWeather Details for {city_name.title()}:")
        print(f"{'-'*40}")
        print(f"Temperature      : {temperature}°C")
        print(f"Feels Like       : {feels_like_temp}°C")
        print(f"Humidity         : {humidity}%")
        print(f"Weather          : {weather} ({description})")
        print(f"Wind Speed       : {wind_speed} m/s")
        print(f"Wind Direction   : {wind_angle}°")
        print(f"{'-'*40}\n")

    except requests.Timeout:
        print("Request timed out. Please try again.")
    except requests.ConnectionError:
        print("Network error. Check your connection.")
    except requests.HTTPError:
        print(f"City '{city}' not found or API error occurred.")


if __name__ == "__main__":
    city = input("Enter a city: ")
    fetch_weather_details(city)
