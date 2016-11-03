import requests
import json
'''
	Get stops data information from cumtd website api
'''

API_KEY = "540c9808c82b43928e0c63aeed553f33"
STOPS_DATA_URL = "https://developer.cumtd.com/api/v2.2/JSON/GetStops"

parameters = {"key" : API_KEY}
response = requests.get(STOPS_DATA_URL, params=parameters)
data = response.json()
with open("data.json", "w") as outfile:
	json.dump(data, outfile, indent=4, sort_keys=True)