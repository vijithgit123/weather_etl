# extractor.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherExtractor:
    def __init__(self, api_key, base_url, units="metric"):
        self._api_key = api_key      # underscore = "internal use" convention (encapsulation)
        self._base_url = base_url
        self._units = units

    def extract_city(self, city):
        """Fetch raw weather data for a single city."""
        params = {
            "q": city,
            "appid": self._api_key,
            "units": self._units
        }
        response = requests.get(self._base_url, params=params)
        response.raise_for_status()  # raises an error if status isn't 200
        return response.json()

    def extract_many(self, cities):
        """Fetch raw weather data for multiple cities."""
        results = []
        for city in cities:
            data = self.extract_city(city)
            results.append(data)
        return results