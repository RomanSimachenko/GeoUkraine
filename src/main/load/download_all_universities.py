from .download_and_read_regions import read_regions_info
import wget
import os
from urllib.error import HTTPError
from .config import UNIVERSITY_PATH, UNIVERSITY_URL, UNIVERSITIES_PATH
from .exceptions import CantDownloadCertainUniversity, CantDownloadRegions
import shutil


def _download_university(un_path: str, un_url: str) -> None:
    """Downloads university as json by the given url"""
    try:
        wget.download(un_url, un_path)
    except HTTPError:
        pass

def download_universities() -> None:
    """Downloads all the universities as json files"""
    try:
        regions = read_regions_info()
    except CantDownloadRegions:
        print("Failed to get regions")
        exit(1)

    shutil.rmtree(UNIVERSITIES_PATH)
    os.mkdir(UNIVERSITIES_PATH)

    for region in regions:
        try:
            _download_university(
                    UNIVERSITY_PATH.format(region.id, region.name), 
                    UNIVERSITY_URL.format(region.id)
                )
        except:
            raise CantDownloadCertainUniversity


if __name__ == "__main__":
    download_universities()
