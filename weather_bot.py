import requests

print("----------------------")
print("     Weather Bot      ")
print("----------------------")

city = input("Enter your city name : ")

url = f"https://wttr.in/{city}?format=j1"

print("Finding your city.......")
response = requests.get(url) #Fething data from API

data = response.json()     #Change JSON to dictionary
weather = data["current_condition"][0]
temperature = weather["temp_C"]
feels_like = weather["FeelsLikeC"]
description = weather["weatherDesc"][0]["value"]

print("--------------------------")
print(f"City : {city.upper()}")
print(f'Temperature : {temperature}C (feels like {feels_like}C)')
print(f'Condition : {description}')
print("---------------------------")