from datetime import datetime
from fastapi import APIRouter, Response
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.service.OpenMeteoService import OpenMeteoService

open_meteo_router = APIRouter(prefix="/open-meteo", tags=["weather"])
open_meteo_service = OpenMeteoService()
scheduler = AsyncIOScheduler()


@open_meteo_router.on_event("startup")
async def start_scheduler():
    """
    Start the scheduler
    :return:
    """
    scheduler.add_job(open_meteo_service.fetch_weather_data, "interval", minutes=5, next_run_time=datetime.now())
    scheduler.start()


@open_meteo_router.get("/metrics", description="Return metrics for given lat and lon")
async def get_weather():
    """
    Get the weather data
    :return:
    """
    return Response(content=open_meteo_service.weather_data, media_type="text/plain")
