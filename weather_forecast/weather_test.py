# # Imports required modules
# import requests
# import json
# import os

# # API_KEY from openweather
# key = "bd5e378503939ddaee76f12ad7a97608"

# # Base URL for openweather
# baseUrl = "http://api.openweathermap.org/data/2.5/weather?"

# # Fetches location from the user
# loc = input("Enter city/state name : ")

# # Creates a final url for requests from server
# url = baseUrl + "appid=" + key + "&q=" + loc

# # To convert json format to python format
# response = requests.get(url)

# # Python format data
# res = response.json()

# # Check whether or not the city was found
# if (res["cod"] == "404"):
# 	print(" Location Not Found ")
# else:
# 	# Gets temperature in Kelvin
# 	tempK = res["main"]["temp"]
# 	# Gets the real feel of the weather
# 	feelK = res["main"]["feels_like"]
# 	# Gets pressure in hectopascals (HPa)
# 	pres = res["main"]["pressure"]
# 	# Gets humidity in percentage
# 	humi = res["main"]["humidity"]
# 	# Gets weather description
# 	desc = res["weather"][0]["description"]

# 	# Converting temperatures from Kelvin to Celcius
# 	tempC = tempK - 273.15
# 	feelC = feelK - 273.15
# 	# Converting pressure from hPa to atm
# 	pres *= 0.0009869233

# 	# Printing all the results & data to the console
# 	print(" Temperature = " + str(round(tempC, 2)) + " °C")
# 	print(" Feels Like = " + str(round(feelC, 2)) + " °C")
# 	print(" Pressure = " + str(round(pres, 2)) + " atm")
# 	print(" Humidity = " + str(humi) + " %")
# 	print(" Description = " + str(desc))

# 	# Runs the shell command to get weather information from wttr.in
# 	print(os.popen(f"curl wttr.in/{loc}").read())
