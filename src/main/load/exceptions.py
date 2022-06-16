class CantDownloadRegions(Exception):
    """Program can't download regions as an excel file from the site"""


class CantDownloadCertainUniversity(Exception):
    """Program can't download a certain university as a json file from the site"""


class CantCreateNewUniversityObjectInDB(Exception):
    """Program can't create a new university object in a Django DataBase"""


class CantGetPlaceIDandCoordinates(Exception):
    """Program can't get a place id, latitude and longitude"""
