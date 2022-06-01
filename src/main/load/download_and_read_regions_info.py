import wget
from django.conf import settings
import os
from typing import NamedTuple
import pandas


class Regions(NamedTuple):
    id: int
    name: str


def download_regions():
    """Downloads regions info as excel file"""
    regions_path = str(settings.BASE_DIR) + "/src/main/load/data/regions.xlsx"

    if os.path.exists(regions_path):
        os.remove(regions_path)

    regions_url = "https://registry.edbo.gov.ua/files/regions.xlsx"
    wget.download(regions_url, regions_path)


def read_regions_info() -> tuple:
    """Reads region IDs and names from downloaded excel file"""
    download_regions()

    regions_path = str(settings.BASE_DIR) + "/src/main/load/data/regions.xlsx"

    excel_data = pandas.read_excel(regions_path)

    ids = excel_data["Код регіону"].tolist()
    names = excel_data["Назва регіону"].tolist()

    regions = ()

    for index in range(len(ids)):
        regions += (Regions(ids[index], names[index].strip()),)

    return regions
