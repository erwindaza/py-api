import requests
import json
#from flask import Flask, jsonify, request
from os import environ

api_key = "3ba3838b0982065ea23087d4d3e68520"
lat = "48.208176"
lon = "16.373819"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
    lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)
