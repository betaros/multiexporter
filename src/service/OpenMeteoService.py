import openmeteo_requests

import requests_cache
from retry_requests import retry

from src.utils.location import Location
from src.utils.metric import create_metric


class OpenMeteoService:
    def __init__(self):
        self.weather_data = ""
        self.location = Location()
        self.lat, self.lon, self.city = self.location.get_position()

    def collect_data(self):
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        openmeteo = openmeteo_requests.Client(session = retry_session)

        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            "current": ["temperature_2m", "relative_humidity_2m", "rain", "showers", "snowfall", "cloud_cover", "pressure_msl", "surface_pressure", "wind_speed_10m", "wind_direction_10m"],
            "timezone": "Europe/Berlin",
            "forecast_days": 1,
            "models": "best_match"
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
        print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        print(f"Elevation {response.Elevation()} m asl")
        print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        # Current values. The order of variables needs to be the same as requested.
        current = response.Current()

        current_data = {
            "current_temperature_2m": current.Variables(0).Value(),
            "current_relative_humidity_2m": current.Variables(1).Value(),
            "current_rain": current.Variables(2).Value(),
            "current_showers": current.Variables(3).Value(),
            "current_snowfall": current.Variables(4).Value(),
            "current_cloud_cover": current.Variables(5).Value(),
            "current_pressure_msl": current.Variables(6).Value(),
            "current_surface_pressure": current.Variables(7).Value(),
            "current_wind_speed_10m": current.Variables(8).Value(),
            "current_wind_direction_10m": current.Variables(9).Value()
        }

        return current_data

    async def fetch_weather_data(self):
        """
        Fetch weather data from Open-Meteo API and create metric
        :return:
        """
        data = self.collect_data()
        metric = create_metric("openmeteo", data, "location", self.city)
        self.weather_data = '\n'.join(metric)
