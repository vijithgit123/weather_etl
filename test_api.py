import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OWM_API_KEY")
CITY = "London"

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.json())