import requests

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {city}: Temperature: {temperature}°C, Humidity: {humidity}%")
    else:
        print("Failed to fetch data")

def main():
    cities = ["Beijing", "Shanghai", "Hangzhou", "Xian", "Dalian"]
    for city in cities:
        print(f"Fetching weather data for {city}")
        fetch_weather_data(city)
