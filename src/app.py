from datetime import datetime
from fastapi import FastAPI, Response, Request
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import uvicorn
import reverse_geocode
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from service.OpenMeteoService import collect_data

from src.utils.metric import create_metric
from src.controller.OpenMeteoController import open_meteo_router

app = FastAPI()
app.include_router(open_meteo_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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
    metric = create_metric("openmeteo", data, location)
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
    return Response(content=weather_data, media_type="text/plain")


@app.get("/")
async def root(request: Request):
    context = {
        "request": request,
        "message": "Hello, World!",
        "lat": lat,
        "lon": lon
    }
    return templates.TemplateResponse("index.html", context)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=9111, log_level="info")