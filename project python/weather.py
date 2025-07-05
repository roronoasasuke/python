import requests

city = str(input("Enter your city :"))
api = "cbc393ab8128269f24bc698c969f0025"


geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api}'
geo_response = requests.get(geo_url).json()
if geo_response:
    lat = geo_response[0]['lat']
    lon = geo_response[0]['lon']

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric'
    weather_response = requests.get(url).json()

    if weather_response.get("cod") == 200:
        print(f'weather in {city} is {weather_response["weather"][0]["description"]}')
        print(f'temperature in {city} is {weather_response["main"]["temp"]}')
    else:
        print('Error fetching weather data.')
else:
    print(f"Could not find coordinates for {city}. Please check the city name.")