import requests
from pprint import pprint

# api-endpoint
url = "http://maps.googleapis.com/maps/api/geocode/json"

# location
location = "delhi technological university"

# params
params = {'address':location}

# sending the request
r = requests.get(url = url, params = params)

# the JSON data
data = r.json()

# extracting fields from the JSON
lat = data['results'][0]['geometry']['location']['lat']
lng = data['results'][0]['geometry']['location']['lng']
address = data['results'][0]['formatted_address']

print("Latitude: %s\nLongitude: %s\nFormatted Address: %s" \
       % (lat, lng, address))
