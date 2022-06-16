import wget
import os
from typing import NamedTuple
from pandas import read_excel
from .config import REGIONS_PATH, REGIONS_URL
from .exceptions import CantDownloadRegions
from typing import List, Tuple


class Region(NamedTuple):
    id: int
    name: str


def download_regions() -> None:
    """Downloads regions info as excel file"""
    if os.path.exists(REGIONS_PATH):
        os.remove(REGIONS_PATH)

    try:
        wget.download(REGIONS_URL, REGIONS_PATH)
    except:
        raise CantDownloadRegions


def _get_region_ids_and_names() -> Tuple[List[int], List[str]]:
    """Gets region ids and names from the downloaded excel file"""
    excel_data = read_excel(REGIONS_PATH)

    ids = excel_data["Код регіону"].tolist()
    names = excel_data["Назва регіону"].tolist()

    return ids, names


def _make_regions(ids: List[int], names: List[str]) -> Tuple[Region, ...]:
    """Makes a tuple of Regions using their ids and names"""
    return tuple((Region(ids[index], names[index]) for index in range(min(len(ids), len(names)))))


def read_regions_info() -> Tuple[Region, ...]:
    download_regions()

    ids, names = _get_region_ids_and_names()

    return _make_regions(ids, names)


if __name__ == "__main__":
    print(read_regions_info())
