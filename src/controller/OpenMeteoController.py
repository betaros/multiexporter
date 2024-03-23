from fastapi import APIRouter

open_meteo_router = APIRouter(prefix="/open-meteo", tags=["weather"])


@open_meteo_router.get("/", description="Get weather")
async def read_open_meteo():
    return {"status": "ok"}


@open_meteo_router.get("/config", description="Return current configuration")
async def get_config():
    return {"lat": "12", "lon": "10"}


@open_meteo_router.post("/config", description="Set configuration")
async def set_config(lat: float, lon: float):
    return {"lat": lat, "lon": lon}


@open_meteo_router.get("/location", description="Return location for given lat and lon")
async def config(lat: float, lon: float):
    return {"lat": lat, "lon": lon}
