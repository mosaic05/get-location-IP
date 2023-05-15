
#FETCH ADDRESS AND ZIP CODE
#import module
from geopy.geocoders import Nominatim
import re
import json
from urllib.request import urlopen
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")


url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print ('Your IP detail\n ')
print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))

place = city+", "+ region
location = geolocator.geocode(place)
print(location)