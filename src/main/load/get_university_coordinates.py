from typing import NamedTuple
import os
import requests


class Coordinates(NamedTuple):
    lat: float
    lng: float


def get_coordinates(university_name: str, university_address: str, region_name: str, koatuu_name: str) -> Coordinates:
    url = f"""https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="{region_name};%20{koatuu_name};%20{university_address}"&inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname%2Cplace_id&key={os.getenv('GOOGLE_API_KEY')}"""
    response = requests.get(url).json()

    try:
        place_id, lat, lng = response['candidates'][0]['place_id'], response['candidates'][0]['geometry']['location']['lat'], response['candidates'][0]['geometry']['location']['lng']
    except IndexError:
        url = f"""https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="{region_name};%20{koatuu_name};%20{university_name}"&inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname%2Cplace_id&key={os.getenv('GOOGLE_API_KEY')}"""
    response = requests.get(url).json()

    place_id, lat, lng = response['candidates'][0]['place_id'], response['candidates'][0]['geometry']['location']['lat'], response['candidates'][0]['geometry']['location']['lng']

    return place_id.strip(), Coordinates(lat, lng)