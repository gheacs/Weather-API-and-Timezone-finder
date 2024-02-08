import requests

def get_weather_data(location):
    api_key = "51113f0fcdccf7fa5ffed32a6724075e"  # Replace with your actual API key from OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # You can change the units to "imperial" for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        # Extract the required weather data from the response
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        # Return the weather data
        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description
        }
    else:
        # Return None if there was an error in fetching the weather data
        return None

