from fastapi import FastAPI, Request
import requests
from geopy.geocoders import Nominatim

app = FastAPI()

@app.get("/location")
async def get_location(request: Request):
    # Get the user's IP address
    client_host = request.client.host
    
    # Use a geocoding service to get location data
    response = requests.get(f"https://ipinfo.io/{client_host}/json")
    location_data = response.json()
    
    # Extract latitude and longitude
    loc = location_data.get("loc", "0,0").split(",")
    latitude, longitude = loc[0], loc[1]
    
    # Use geopy to get more detailed location information
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    
    return {
        # "ip": client_host,
        
        "latitude": latitude,
        "longitude": longitude,
        "address": location.address if location else "Address not found"
    }
