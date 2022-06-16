import json
from typing import List
from .. import models
from .download_all_universities import download_universities
from .get_university_coordinates import get_coordinates
import os
from django.core.exceptions import ObjectDoesNotExist
from .config import UNIVERSITIES_PATH
from .exceptions import CantDownloadCertainUniversity, CantCreateNewUniversityObjectInDB, CantGetPlaceIDandCoordinates
from .config import University


def process_regions() -> None:
    """Processes regions"""
    region_json_names = os.listdir(UNIVERSITIES_PATH)

    for name in region_json_names:
        print(name)
        with open(UNIVERSITIES_PATH + '/' + name) as file:
            json_data = json.load(file)

        region_id, region_name = (item.strip() for item in name.split(':'))
        region_id, region_name = int(region_id), region_name.split('.')[0].strip()
        region = models.Regions.objects.get_or_create(id=region_id, name=region_name)[0]
        
        try:
            seed_db(json_data, region)
        except CantCreateNewUniversityObjectInDB:
            print("Failed to seed a certain university")
            exit(1)

        break # only for 1 region


def seed_db(data: List[dict], region: models.Regions) -> None:
    """Loads Django data base using taken data"""
    for university in data:
        un_data = University.parse_obj(university)

        try:
            place_id, coordinates = get_coordinates(un_data.name, un_data.address, 
                    un_data.region_name, un_data.koatuu_name)
        except CantGetPlaceIDandCoordinates:
            print("Failed to get place id or coordinates")
            exit(1)

        try:
            old_un = models.Universities.objects.get(id=un_data.id)
            old_un.delete()
        except ObjectDoesNotExist:
            pass

        result_un_dict = un_data.dict()
        result_un_dict['place_id'] = place_id
        result_un_dict['lat'] = coordinates.lat
        result_un_dict['lng'] = coordinates.lng

        try:
            un = models.Universities.objects.create(**result_un_dict)
        except:
            print(result_un_dict['name'])
            raise CantCreateNewUniversityObjectInDB

        region.universities.add(un)


# Run the `main` function from the Django shell (python3 manage.py shell)!!!
def main() -> None:
    try:
        download_universities()
    except CantDownloadCertainUniversity:
        print("Failed to download a certain university")
        exit(1)

    process_regions()


