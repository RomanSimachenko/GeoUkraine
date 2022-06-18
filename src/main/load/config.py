from django.conf import settings
import os

REGIONS_PATH = str(settings.BASE_DIR) + "/src/main/load/data/regions.xlsx"

REGIONS_URL = "https://registry.edbo.gov.ua/files/regions.xlsx"

UNIVERSITY_PATH = str(settings.BASE_DIR) + "/src/main/load/data/universities/{}: {}.json"

UNIVERSITY_URL = "https://registry.edbo.gov.ua/api/universities/?ut=1&lc={}&exp=json"

UNIVERSITIES_PATH = str(settings.BASE_DIR) + "/src/main/load/data/universities"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
