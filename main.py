import requests
from datetime import datetime

MY_LAT = 42.874622
MY_LONG = 74.569763

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response.status_code)
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
  'lat': MY_LAT,
  'lng': MY_LONG,
  'formatted': 0,
}

reponse = requests.get('https://api.sunrise-sunset.org/json',
                       params=parameters)
reponse.raise_for_status()
data = reponse.json()
print(data)

sunrise = data['results']['sunrise']
sunset = data['results']['sunrise']
print(sunrise)
print(sunrise.split('T'))
# print(sunset)

time_now = datetime.now()
# print(time_now.hour)
