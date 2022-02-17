import requests
import json
import pandas as pd
from datetime import datetime, timezone
import pyowm
from pyowm.commons.exceptions import NotFoundError
#from flask import Flask, jsonify, request
from os import environ

# APIKEY = '3ba3838b0982065ea23087d4d3e68520'  # your API Key here as string
# OpenWMap = pyowm.OWM(APIKEY)                   # Use API key to get data
# # give where you need to see the weather
# Weather = OpenWMap.weather_at_place('London')
# # get out data in the mentioned location
# Data = Weather.get_weather()
# ########################################################################################################
# api_key = "3ba3838b0982065ea23087d4d3e68520"
# lat = "48.208176"
# lon = "16.373819"
# url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
#     lat, lon, api_key)
# response = requests.get(url)
# json_data = json.loads(response.text)
# print(json_data)
# ########################################################################################################


City_API_endpoint = "http://api.openweathermap.org/data/2.5/weather?q="
City = "Nairobi"
Country = ",KE,"
join_key = "&appid=" + "3ba3838b0982065ea23087d4d3e68520"
units = "&units=metric"

current_city_weather = City_API_endpoint + City + Country + join_key + units
# print(current_city_weather)

json_data = requests.get(current_city_weather).json()
# print(json_data)


df_all_current_weather = pd.DataFrame()

# Create empty lists to store the JSON Data
current_weather_id = []
current_time = []
own_city_id = []
city = []
latitude = []
longitude = []
country = []
timezone = []
sunrise = []
sunset = []
temperature = []
temperature_feel = []
temperature_min = []
temperature_max = []
pressure = []
humidity = []
main = []
main_description = []
clouds = []
wind_speed = []
wind_degree = []
visibility = []

# Add JSON Data to the lists
# prediction_num += 1
# current_weather_id.append(prediction_num + 1)
current_time.append(pd.Timestamp.now())
own_city_id.append(json_data['id'])
city.append(json_data['name'])
latitude.append(json_data['coord']['lat'])
longitude.append(json_data['coord']['lon'])
country.append(json_data['sys']['country'])
if json_data['timezone'] > 0:
    timezone.append(("+" + str((json_data['timezone'])/3600)))
else:
    timezone.append(((json_data['timezone'])/3600))
sunrise.append(json_data['sys']['sunrise'])
sunset.append(json_data['sys']['sunset'])
temperature.append(json_data['main']['temp'])
temperature_feel.append(json_data['main']['feels_like'])
temperature_min.append(json_data['main']['temp_min'])
temperature_max.append(json_data['main']['temp_max'])
pressure.append(json_data['main']['pressure'])
humidity.append(json_data['main']['humidity'])
main.append(json_data['weather'][0]['main'])
main_description.append(json_data['weather'][0]['description'])
clouds.append(json_data['clouds']['all'])
wind_speed.append(json_data['wind']['speed'])
wind_degree.append(json_data['wind']['deg'])
visibility.append(json_data['visibility'])

# Write Lists to DataFrame
df_all_current_weather['current_weather_id'] = current_weather_id
df_all_current_weather['current_time'] = current_time
df_all_current_weather['own_city_id'] = own_city_id
df_all_current_weather['city'] = city
df_all_current_weather['latitude'] = latitude
df_all_current_weather['longitude'] = longitude
df_all_current_weather['country'] = country
df_all_current_weather['timezone'] = timezone
df_all_current_weather['sunrise'] = sunrise
df_all_current_weather['sunset'] = sunset
df_all_current_weather['temperature'] = temperature
df_all_current_weather['temperature_feel'] = temperature_feel
df_all_current_weather['temperature_min'] = temperature_min
df_all_current_weather['temperature_max'] = temperature_max
df_all_current_weather['pressure'] = pressure
df_all_current_weather['humidity'] = humidity
df_all_current_weather['main'] = main
df_all_current_weather['main_description'] = main_description
df_all_current_weather['clouds'] = clouds
df_all_current_weather['wind_speed'] = wind_speed
df_all_current_weather['wind_degree'] = wind_degree
df_all_current_weather['visibility'] = visibility

print(df_all_current_weather.head(5))


# with open('database.json', 'w') as archive:
#     json.dump(database, archive)
#     print("Archive exported")
