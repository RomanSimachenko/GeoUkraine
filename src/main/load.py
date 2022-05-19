import json
from typing import List
from . import models
from django.conf import settings


def read_json_data(file_path: str) -> List:
    """Reads and returns loaded json as a list"""
    with open(settings.BASE_DIR / file_path) as file:
        json_data = json.load(file)

    return json_data


def seed_db(data: List) -> str:
    """Seeds Django data base using taken data"""
    try:
        for university in data:
            university_dict = {
                "id": int(university['university_id']),
                "name": university['university_name'],
                "phone": university['university_phone'],
                "email": university['university_email'],
                "address": university['university_address'],
                "type_name": university['university_type_name'],
                "registration_year": university['registration_year'],
                "edrpou": university['university_edrpou'],
                "post_index": university['post_index'],
                "koatuu_id": university['koatuu_id'],
                "region_name": university['region_name'],
                "koatuu_name": university['koatuu_name'],
                "is_from_crimea": True if university['is_from_crimea'].strip().lower() == "так" else False
            }

            models.Universities.objects.create(**university_dict)
    except Exception as error:
        return f"[ERROR] {error}"

    return "[INFO] Data loaded successfully!"


# Run the `main` function from the Django shell!!!
def main():
    file_path = input(
        "Json file path(from root of the project, json file must be in the project package): ").strip()

    json_data = read_json_data(file_path=file_path)

    print(seed_db(json_data))
