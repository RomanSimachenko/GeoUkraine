import wget
from django.conf import settings
import os
from typing import NamedTuple
import pandas


REGIONS_PATH = str(settings.BASE_DIR) + "/src/main/load/data/regions.xlsx"

REGIONS_URL = "https://registry.edbo.gov.ua/files/regions.xlsx"


class Regions(NamedTuple):
    id: int
    name: str


def download_regions():
    """Downloads regions info as excel file"""
    if os.path.exists(REGIONS_PATH):
        os.remove(REGIONS_PATH)

    wget.download(REGIONS_URL, REGIONS_PATH)


def read_regions_info() -> tuple:
    """Reads region IDs and names from downloaded excel file"""
    download_regions()

    excel_data = pandas.read_excel(REGIONS_PATH)

    ids = excel_data["Код регіону"].tolist()
    names = excel_data["Назва регіону"].tolist()

    regions = ()

    for index in range(len(ids)):
        regions += (Regions(ids[index], names[index].strip()),)

    return regions
