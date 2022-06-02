from django.conf import settings
from .download_and_read_regions_info import read_regions_info
import wget
import os
from urllib.error import HTTPError


UNIVERSITY_PATH = str(settings.BASE_DIR) + "/src/main/load/data/universities/{}: {}.json"

UNIVERSITY_URL = "https://registry.edbo.gov.ua/api/universities/?ut=1&lc={}&exp=json"


def download_universities():
    """Download all the universities as json"""
    regions = read_regions_info()

    for region in regions:
        now_un_path = UNIVERSITY_PATH.format(region.id, region.name)
        now_un_url = UNIVERSITY_URL.format(region.id)

        if os.path.exists(now_un_path):
            os.remove(now_un_path)

        try:
            wget.download(now_un_url, now_un_path)
        except HTTPError:
            continue
