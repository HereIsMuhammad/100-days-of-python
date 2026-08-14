# Day 72: Working with APIs

import requests

# Example 1: Fetch random user data
url = "https://randomuser.me/api/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    user = data['results'][0]
    print("Random User Data:")
    print("Name:", user['name']['first'], user['name']['last'])
    print("Email:", user['email'])
    print("Country:", user['location']['country'])
else:
    print("Failed to fetch data")

print("\n")

# Example 2: Fetch weather data (OpenWeatherMap API free)
# You need to register for a free API key at https://openweathermap.org/api
# api_key = "YOUR_API_KEY"
# city = "London"
# weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
# response = requests.get(weather_url)
# if response.status_code == 200:
#     weather_data = response.json()
#     print(f"Weather in {city}: {weather_data['main']['temp']}°C, {weather_data['weather'][0]['description']}")
# else:
#     print("Failed to fetch weather data")