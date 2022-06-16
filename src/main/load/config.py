from django.conf import settings
from pydantic import BaseModel, Field
import os
from typing import Optional

REGIONS_PATH = str(settings.BASE_DIR) + "/src/main/load/data/regions.xlsx"

REGIONS_URL = "https://registry.edbo.gov.ua/files/regions.xlsx"

UNIVERSITY_PATH = str(settings.BASE_DIR) + "/src/main/load/data/universities/{}: {}.json"

UNIVERSITY_URL = "https://registry.edbo.gov.ua/api/universities/?ut=1&lc={}&exp=json"

UNIVERSITIES_PATH = str(settings.BASE_DIR) + "/src/main/load/data/universities"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")


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
    koatuu_id: int = Field(alias='koatuu_id')
    region_name: str
    koatuu_name: str
    address: str = Field(alias='university_address')
    post_index_u: int = Field(alias='post_index_u')
    koatuu_id_u: int = Field(alias='koatuu_id_u')
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


