from datetime import datetime


class WeatherTransformer:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._cleaned_data = []

    def clean(self):
        """Extract and normalize the fields we care about from raw API responses."""
        cleaned = []
        for entry in self._raw_data:
            record = {
                "city": entry.get("name"),
                "temp": entry.get("main", {}).get("temp"),
                "humidity": entry.get("main", {}).get("humidity"),
                "wind_speed": entry.get("wind", {}).get("speed"),
                "rain_1h": entry.get("rain", {}).get("1h", 0),
                "timestamp": self._convert_timestamp(entry.get("dt")),
            }
            cleaned.append(record)
        self._cleaned_data = cleaned
        return self._cleaned_data

    @staticmethod
    def _convert_timestamp(unix_time):
        """Pure utility: convert Unix timestamp to a readable datetime string."""
        if unix_time is None:
            return None
        return datetime.utcfromtimestamp(unix_time).strftime("%Y-%m-%d %H:%M:%S")

    def aggregate(self):
        """Compute summary stats across all cleaned records."""
        if not self._cleaned_data:
            raise ValueError("No cleaned data available. Call clean() first.")

        temps = [r["temp"] for r in self._cleaned_data if r["temp"] is not None]

        summary = {
            "avg_temp": round(sum(temps) / len(temps), 2),
            "max_temp": max(temps),
            "min_temp": min(temps),
            "city_count": len(self._cleaned_data),
        }
        return summary