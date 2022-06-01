from typing import NamedTuple
import os
import requests


class Coordinates(NamedTuple):
    lat: float
    lng: float


def get_coordinates(university_name: str, university_address: str, region_name: str, koatuu_name: str) -> Coordinates:
    url = f"""https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="{region_name};%20{koatuu_name};%20{university_address}"&inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname&key={os.getenv('GOOGLE_API_KEY')}"""
    response = requests.get(url).json()

    try:
        lat, lng = response['candidates'][0]['geometry']['location']['lat'], response['candidates'][0]['geometry']['location']['lng']
    except IndexError:
        url = f"""https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="{region_name};%20{koatuu_name};%20{university_name}"&inputtype=textquery&fields=formatted_address%2Cgeometry%2Cname&key={os.getenv('GOOGLE_API_KEY')}"""
    response = requests.get(url).json()

    lat, lng = response['candidates'][0]['geometry']['location']['lat'], response['candidates'][0]['geometry']['location']['lng']

    return Coordinates(lat, lng)
