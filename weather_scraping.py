from bs4 import BeautifulSoup
#importing requests module
import requests
from influxdb import InfluxDBClient

#header user agent is a string allows the server to identify the O.S and application
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS\
          X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko)\
          Chrome/71.0.3578.98 Safari/537.36",
          "Accept":"text/html,application/xhtml+xml,application/xml;\
          q=0.9,image/webp,image/apng,*/*;q=0.8"}

# InfluxDB connection settings
influx_client = InfluxDBClient(host='INFLUXDB_HOST', port=8086)
influx_client.switch_database('YOUR_DATABASE_NAME')

#defining the weather function
def weather(city):
# Replaces the space with + operator
    city=city.replace(" ","+")
#requests and get function to get the information from the URL provided
    res=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
#Navigates on that particular website ,extract and store the data in soup object
    soup = BeautifulSoup(res.text,'html.parser')
#gets the weather information, weatehr and humidity
    temp = soup.select('#wob_tm')[0].getText().strip()
    hunidity = soup.select('#wob_hm')[0].getText().strip()
    return temp, hunidity

#enter the city name
city="Santa Marta"

#Concatenating the city name and weather 
city=city+" weather"

temp, humidity = weather(city)

json_body = [
    {
        "measurement": "weather",
        "fields": {
            "temperature": temp,
            "humidity": humidity
        }
    }
]

print(json_body)

#Write the data point to InfluxDB
influx_client.write_points(json_body)