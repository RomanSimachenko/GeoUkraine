from typing import NamedTuple, Tuple
import requests
from .config import GOOGLE_API_KEY
from .exceptions import CantGetPlaceIDandCoordinates

first_api_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" \
    "input={}%2B{}%2B{}&" \
    "inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname%2Cplace_id&" \
    f"key={GOOGLE_API_KEY}"

second_api_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" \
    "input={}%2B{}%2B{}&" \
    "inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname%2Cplace_id&" \
    f"key={GOOGLE_API_KEY}"
 

class Coordinates(NamedTuple):
    lat: float
    lng: float


def throw_request_to_google_api_by_url(url: str) -> Tuple[str, float, float]:
    """
    Sends a request to the Google API by given url
    Returns place id, latitude and longitude
    """
    response = requests.get(url).json()

    place_id = response['candidates'][0]['place_id']
    lat, lng = response['candidates'][0]['geometry']['location']['lat'], response['candidates'][0]['geometry']['location']['lng']

    return place_id, lat, lng


def get_coordinates(university_name: str, university_address: str, region_name: str, koatuu_name: str) -> Tuple[str, Coordinates]:
    """Gets university place_id and coordinates"""
    try:
        try:
            place_id, lat, lng = throw_request_to_google_api_by_url(first_api_url.format(region_name, koatuu_name, university_address))
        except IndexError:
            place_id, lat, lng = throw_request_to_google_api_by_url(second_api_url.format(region_name, koatuu_name, university_name))
    
        return place_id.strip(), Coordinates(lat, lng)
    except:
        raise CantGetPlaceIDandCoordinates

