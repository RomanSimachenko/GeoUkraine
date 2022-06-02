from typing import NamedTuple
import os
import requests


class Coordinates(NamedTuple):
    lat: float
    lng: float


def get_coordinates(university_name: str, university_address: str, region_name: str, koatuu_name: str):
    """Gets university place_id and coordinates putting reqeust to Google API"""
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" \
        f"input={region_name}%2B{koatuu_name}%2B{university_address}&" \
        "inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname%2Cplace_id&" \
        f"key={os.getenv('GOOGLE_API_KEY')}"
    response = requests.get(url).json()

    try:
        place_id = response['candidates'][0]['place_id']
        lat, lng = response['candidates'][0]['geometry']['location']['lat'], response['candidates'][0]['geometry']['location']['lng']
    except IndexError:
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" \
            f"input={region_name}%2B{koatuu_name}%2B{university_name}&" \
            "inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname%2Cplace_id&" \
            f"key={os.getenv('GOOGLE_API_KEY')}"
    response = requests.get(url).json()

    place_id = response['candidates'][0]['place_id']
    lat, lng = response['candidates'][0]['geometry']['location']['lat'], response['candidates'][0]['geometry']['location']['lng']

    return place_id.strip(), Coordinates(lat, lng)
