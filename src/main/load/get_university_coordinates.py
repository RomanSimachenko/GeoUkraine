from typing import NamedTuple
import requests
from .config import API_URL
from .exceptions import CantGetPlaceIDandCoordinates


class Coordinates(NamedTuple):
    lat: float
    lng: float


def throw_request_to_google_api_by_url(url: str) -> tuple[str, float, float]:
    """
    Sends a request to the Google API by given url
    Returns place id, latitude and longitude
    """
    response = requests.get(url).json()

    place_id = response['candidates'][0]['place_id']
    lat, lng = response['candidates'][0]['geometry']['location']['lat'], \
        response['candidates'][0]['geometry']['location']['lng']

    return place_id, lat, lng


def get_coordinates(university_name: str, university_address: str, 
        region_name: str, koatuu_name: str) -> tuple[str, Coordinates]:
    """Gets university place_id and coordinates"""
    try:
        try:
            place_id, lat, lng = throw_request_to_google_api_by_url(API_URL.format(region_name, 
                koatuu_name, university_address))
        except IndexError:
            place_id, lat, lng = throw_request_to_google_api_by_url(API_URL.format(region_name, 
                koatuu_name, university_name))
    
        return place_id.strip(), Coordinates(lat, lng)
    except:
        raise CantGetPlaceIDandCoordinates

