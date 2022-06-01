import json
from typing import List
from .. import models
from django.conf import settings
from .download_all_universities import download_universities
from .get_university_coordinates import get_coordinates
import os
from django.core.exceptions import ObjectDoesNotExist


def seed_db(data: List, region_id: int, region_name: str):
    """Loads Django data base using taken data"""

    region = models.Regions.objects.get_or_create(
        id=region_id, name=region_name)[0]
    
    for university in data:
        un_id = int(university['university_id'].strip())
        un_name = university['university_name'].strip()
        un_address = university['university_address'].strip()
        un_region_name = university['region_name'].strip()
        un_koatuu_name = university['koatuu_name'].strip()

        place_id, coordinates = get_coordinates(
            un_name, un_address, un_region_name, un_koatuu_name)

        university_dict = {
            "id": un_id,
            "place_id": place_id,
            "name": un_name,
            "phone": university['university_phone'].strip(),
            "email": university['university_email'].strip(),
            "address": un_address,
            "type_name": university['university_type_name'].strip(),
            "edrpou": university['university_edrpou'].strip(),
            "post_index": university['post_index'].strip(),
            "koatuu_id": university['koatuu_id'].strip(),
            "region_name": un_region_name,
            "koatuu_name": un_koatuu_name,
            "is_from_crimea": True if university['is_from_crimea'].strip().lower() == "так" else False,
            "lat": coordinates.lat,
            "lng": coordinates.lng,
            
            "registration_year": university['registration_year'].strip() if university['registration_year'] else None,
            "parent_id": int(university['university_parent_id'].strip()) if university['university_parent_id'] else None,
            "short_name": university['university_short_name'].strip() if university['university_short_name'] else None,
            "name_en": university['university_name_en'].strip() if university['university_name_en'] else None,
            "site": university['university_site'].strip() if university['university_site'] else None,
            "address_u": university['university_address_u'].strip() if university['university_address_u'] else None,
            "financing": university['university_financing_type_name'].strip() if university['university_financing_type_name'] else None,
            "governance": university['university_governance_type_name'].strip() if university['university_governance_type_name'] else None,
            "post_index_u": int(university['post_index_u'].strip()) if university['post_index_u'] else None,
            "koatuu_id_u": int(university['koatuu_id_u'].strip()) if university['koatuu_id_u'] else None,
            "region_name_u": university['region_name_u'].strip() if university['region_name_u'] else None,
            "koatuu_name_u": university['koatuu_name_u'].strip() if university['koatuu_name_u'] else None,
            "director_post": university['university_director_post'].strip() if university['university_director_post'] else None,
            "director_fio": university['university_director_fio'].strip() if university['university_director_fio'] else None,
            "close_date": university['close_date'].strip() if university['close_date'] else None,
            "primitki": university['primitki'].strip() if university['primitki'] else None
        }

        try:
            old_un = models.Universities.objects.get(id=un_id)
            old_un.delete()
        except ObjectDoesNotExist:
            pass

        un = models.Universities.objects.create(**university_dict)

        region.universities.add(un)


# Run the `main` function from the Django shell (python3 manage.py shell)!!!
def main():
    download_universities()

    universities_path = str(settings.BASE_DIR) + \
        "/src/main/load/data/universities"

    university_json_paths = os.listdir(universities_path)

    for path in university_json_paths:
        with open(universities_path + '/' + path) as file:
            json_data = json.load(file)

        region_id, region_name = (item.strip() for item in path.split(':'))
        seed_db(json_data, int(region_id), region_name.split('.')[0].strip())

        break # only for 1 region
