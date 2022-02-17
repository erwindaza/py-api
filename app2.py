import requests
import json
import pandas as pd
from datetime import datetime, timezone
import pyowm
from pyowm.commons.exceptions import NotFoundError
#from flask import Flask, jsonify, request
from os import environ
#	Name	Latitude	Longitude
# 1	Berlin 	52.520007 	13.404954
# 2	London 	-33.448890 	-70.669265
# 3	Rome 	41.902783 	12.496365
# 4	Amsterdam 	52.367573 	4.904139
# 5	Barcelona 	41.387397 	2.168568
# 6	Chicago 	41.878114 	-87.629798
# 7	Dubai 	25.204849 	55.270783
# 8	Edmonton 	53.546124 	-113.493823
# 9	Frankfurt 	50.110922 	8.682127
# 10	Madrid 	40.416775 	-3.703790

date_utc = datetime.now(timezone.utc)


cities = ['Berlin', 'London', 'Rome',  'Amsterdam', 'Barcelona',
          'Chicago', 'Dubai', 'Edmonton', 'Frankfurt', 'Madrid']

for city in cities:
    try:
        APIKEY = "3ba3838b0982065ea23087d4d3e68520"
        w = pyowm.OWM(APIKEY)\
            .weather_manager()\
            .weather_at_place(city)\
            .weather
        print(f"current weather at {city} city:")
        print(f"- Temperature: {w.temperature('celsius')['temp']} \u00b0C")
        print(
            F"- Max Temp. Currently {w.temperature('celsius')['temp_max']} \u00b0C")
        print(
            F"- Min Temp. Currently {w.temperature('celsius')['temp_min']} \u00b0C")
    except NotFoundError:
        print(f"{city} city not found:")

print(date_utc)
