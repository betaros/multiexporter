from datetime import datetime
from fastapi import APIRouter, Response
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.service.EnergyChartsService import EnergyChartsService

energy_charts_router = APIRouter(prefix="/energy-charts", tags=["weather"])
energy_charts_service = EnergyChartsService()
scheduler = AsyncIOScheduler()


@energy_charts_router.on_event("startup")
async def start_scheduler():
    """
    Start the scheduler
    :return:
    """
    scheduler.add_job(energy_charts_service.fetch_energy_data(), "interval", minutes=60, next_run_time=datetime.now())
    scheduler.start()


@energy_charts_router.get("/metrics", description="Return metrics")
async def get_weather():
    """
    Get the weather data
    :return:
    """
    return Response(content=energy_charts_service.weather_data, media_type="text/plain")
