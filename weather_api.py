import requests
import json
import time
#from influxdb import InfluxDBClient

# API key for OpenWeatherMap
api_key = 'ede35f6ce591a9e7197c91de0cf5e351'

# City and country code for the location you want to get weather for
city = 'Santa Marta'
country_code = 'CO'

# InfluxDB connection settings
#influx_client = InfluxDBClient(host='INFLUXDB_HOST', port=8086)
#influx_client.switch_database('YOUR_DATABASE_NAME')

# Make a GET request to the OpenWeatherMap API
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}'
response = requests.get(url)
data = json.loads(response.text)

# Extract temperature and humidity from API response
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]

# Create a new data point for InfluxDB
json_body = [
    {
        "measurement": "weather",
        "fields": {
            "temperature": temperature,
            "humidity": humidity
        }
    }
]

print(json_body)

# Write the data point to InfluxDB
#influx_client.write_points(json_body)