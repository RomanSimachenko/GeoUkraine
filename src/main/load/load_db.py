from .. import models
from .download_all_universities import download_universities
from .get_university_coordinates import get_coordinates
import os
from django.core.exceptions import ObjectDoesNotExist
from .config import UNIVERSITIES_PATH
from .exceptions import CantDownloadCertainUniversity, CantCreateNewUniversityObjectInDB, CantGetPlaceIDandCoordinates
from typing import Optional
from pydantic import BaseModel, Field, parse_raw_as


class University(BaseModel):
    name: str = Field(alias='university_name')
    id: int = Field(alias='university_id')
    parent_id: Optional[int] = Field(alias='university_parent_id')
    short_name: str = Field(alias='university_short_name')
    name_en: str = Field(alias='university_name_en')
    is_from_crimea: str = Field(alias='is_from_crimea')
    registration_year: Optional[int] = Field(alias='registration_year')
    edrpou: int = Field(alias='university_edrpou')
    type_name: str = Field(alias='university_type_name')
    financing: str = Field(alias='university_financing_type_name')
    governance: str = Field(alias='university_governance_type_name')
    post_index: int = Field(alias='post_index')
    katottgcode: str
    region_name: str
    koatuu_name: str
    address: str = Field(alias='university_address')
    post_index_u: int = Field(alias='post_index_u')
    katottgcodeu: str
    region_name_u: str = Field(alias='region_name_u')
    koatuu_name_u: Optional[str] = Field(alias='koatuu_name_u')
    address_u: str = Field(alias='university_address_u')
    phone: str = Field(alias='university_phone')
    email: str = Field(alias='university_email')
    site: str = Field(alias='university_site')
    director_post: str = Field(alias='university_director_post')
    director_fio: str = Field(alias='university_director_fio')
    close_date: Optional[str] = Field(alias='close_date')
    primitki: str = Field(alias='primitki')


def load_universities_from_every_region() -> None:
    """Loads all the universities in each region"""
    region_json_names = os.listdir(UNIVERSITIES_PATH)

    for name in region_json_names:
        print(name)

        json_data = open(UNIVERSITIES_PATH + '/' + name).read().strip()
        universities = parse_raw_as(list[University], json_data)

        region_id, region_name = (item.strip() for item in name.split(':'))
        region_id, region_name = int(region_id), region_name.split('.')[0].strip()

        region = models.Regions.objects.get_or_create(id=region_id, name=region_name)[0]
        
        try:
            seed_db(universities, region)
        except CantCreateNewUniversityObjectInDB:
            print("Failed to seed a certain university")
            exit(1)

        # break # only for 1 region


def seed_db(uns: list[University], region: models.Regions) -> None:
    """Loads Django data base using taken data"""
    for un in uns:
        try:
            place_id, coordinates = get_coordinates(un.name, un.address, 
                    un.region_name, un.koatuu_name)
        except CantGetPlaceIDandCoordinates:
            print("Failed to get place id or coordinates")
            exit(1)

        try:
            old_un = models.Universities.objects.get(id=un.id)
            old_un.delete()
        except ObjectDoesNotExist:
            pass

        result_un_dict = un.dict()
        result_un_dict.update(
                {
                    "place_id": place_id,
                    "lat": coordinates.lat,
                    "lng": coordinates.lng,
                }
            )

        try:
            now_un = models.Universities.objects.create(**result_un_dict)
        except:
            raise CantCreateNewUniversityObjectInDB

        region.universities.add(now_un)


# Call the `main` function from the Django shell (python3 manage.py shell)!!!
def main() -> None:
    try:
        download_universities()
    except CantDownloadCertainUniversity:
        print("Failed to download a certain university")
        exit(1)

    load_universities_from_every_region()
