import os
from dotenv import load_dotenv
from extractor import WeatherExtractor
from transformer import WeatherTransformer
from config import CITIES, UNITS, BASE_URL

load_dotenv()
api_key = os.getenv("OWM_API_KEY")

extractor = WeatherExtractor(api_key, BASE_URL, UNITS)
raw_data = extractor.extract_many(CITIES)

transformer = WeatherTransformer(raw_data)
cleaned = transformer.clean()
summary = transformer.aggregate()

print("Cleaned records:")
for r in cleaned:
    print(r)

print("\nSummary:")
print(summary)