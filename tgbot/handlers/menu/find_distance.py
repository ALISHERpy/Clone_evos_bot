import requests
from dtb.settings import OPENSTREET_DISTANCE
from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim

def get_distance_name(latitude, longitude):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.reverse(f"{latitude}, {longitude}")

    if location:
        location = location.address
        sozlar = location.split(", ")  
        oxirgi_ikki_soz = " ".join(sozlar)  
        return oxirgi_ikki_soz
    return None

def calculate_driving_distance(origin_lat, origin_lon, destination_lat, destination_lon):
    url =OPENSTREET_DISTANCE
    url += f"{origin_lon},{origin_lat};{destination_lon},{destination_lat}"
    
   
    response = requests.get(url)
    response_data = response.json()
    # print(response_data)


    if response_data["code"] == "Ok":
        name = response_data['waypoints'][1]['name']
        distance = response_data['routes'][0]['legs'][0]['distance']
        
        return distance

    return None
    
   

  