# main.py

import os
from dotenv import load_dotenv
from extractor import WeatherExtractor
from config import CITIES, UNITS, BASE_URL

load_dotenv()
api_key = os.getenv("OWM_API_KEY")

extractor = WeatherExtractor(api_key, BASE_URL, UNITS)
raw_data = extractor.extract_many(CITIES)

for entry in raw_data:
    print(entry["name"], "-", entry["main"]["temp"])