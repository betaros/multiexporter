from datetime import datetime

from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import uvicorn
import reverse_geocode

from openmeteo import collect_data
from metric import create_metric

app = FastAPI()
scheduler = AsyncIOScheduler()
weather_data = ""

lat = 53.9288531
lon = 12.3409471

coordinates = ((lat, lon),)
location = reverse_geocode.search(coordinates)[0]['city']


async def fetch_weather_data():
    """
    Fetch weather data from Open-Meteo API and create metric
    :return:
    """
    data = collect_data(lat, lon)
    metric = create_metric(data, location)
    global weather_data
    weather_data = '\n'.join(metric)


@app.on_event("startup")
async def start_scheduler():
    """
    Start the scheduler
    :return:
    """
    scheduler.add_job(fetch_weather_data, "interval", minutes=5, next_run_time=datetime.now())
    scheduler.start()


@app.get("/metrics")
async def get_weather():
    """
    Get the weather data
    :return:
    """
    global weather_data
    return weather_data

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9111, log_level="info")