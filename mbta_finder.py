"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.
"""
import math
from urllib.request import urlopen
import json
import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "YOUR_API_KEY"
# Note: Do NOT save your own API key to GitHub!



# A little bit of scaffolding if you want to use it

def get_json(url):
    """Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urlopen(url)
    response_text = f.read()
    response_data = json.loads(str(response_text, "utf-8"))
    return response_data

def get_lat_long(place_name):
    """Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    name = place_name.replace(' ', '%20')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + name + '&key=YOUR_API_KEY'
    lat_long = get_json(url)["results"][0]["geometry"]["location"]
    return (lat_long['lat'], lat_long['lng'])

def get_nearest_station(latitude, longitude):
    """Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = "https://api-v3.mbta.com/stops?filter[latitude]=" + str(latitude) + "&filter[longitude]=" + str(longitude) + "&key=YOUR_API_KEY"
    station_name = get_json(url)['data'][0]['attributes']['name']
    station_latitude = get_json(url)['data'][0]['attributes']['latitude']
    station_longitude = get_json(url)['data'][0]['attributes']['longitude']
    distance = (math.sqrt(((float(latitude)-station_latitude)**2)+((float(longitude)-station_longitude)**2)))*69
    return (station_name, distance)

def find_stop_near(place_name):
    """Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    print(get_nearest_station(*(get_lat_long(place_name))))

print(get_nearest_station(*(get_lat_long('Fenway Park'))))
