import requests

# API key and url for the website from which to get the required data 
API_KEY = 'b534ef356b156ec919f6afe5bae0cd7d'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

    # Communicates with the website to get weather data based on the city inputed by the user 
    response = requests.get(url)

    #if 
    if response.status_code == 200:
        data = response.json()

        #sorts the daa and picks the required information 
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    
    else:
        print(f"Error {response.status_code}: Could not retrieve data")


city = input("Enter city name: ")
get_weather(city)
