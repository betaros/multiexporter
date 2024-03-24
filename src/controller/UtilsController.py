from fastapi import APIRouter
from src.utils.config import read_config, write_config
from src.utils.location import Location

utils_router = APIRouter(prefix="/utils", tags=["utils"])
location = Location()


@utils_router.get("/config", description="Get config")
async def get_config():
    return read_config()


@utils_router.post("/config", description="Set config")
async def get_config():
    return write_config()


@utils_router.get("/location", description="Get location")
async def get_location():
    lat, lon, city = location.get_position()
    return {
        "latitude": lat,
        "longitude": lon,
        "location": city
    }


@utils_router.post("/location", description="Set location")
async def set_location(latitude: float, longitude: float):
    lat = latitude
    lon = longitude
    location.set_position(lat, lon)
    return get_location()
