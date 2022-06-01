from django.conf import settings
from .download_and_read_regions_info import read_regions_info
import wget
import os
from urllib.error import HTTPError


def download_universities():
    """Download all the universities as json"""
    regions = read_regions_info()

    for region in regions:
        university_path = str(settings.BASE_DIR) + \
            f"/src/main/load/data/universities/{region.id}: {region.name}.json"
        university_url = f"https://registry.edbo.gov.ua/api/universities/?ut=1&lc={region.id}&exp=json"

        if os.path.exists(university_path):
            os.remove(university_path)

        try:
            wget.download(university_url, university_path)
        except HTTPError:
            continue

    print("\n[+] Universities downloaded.\n")
