from fastapi import FastAPI, Request
import uvicorn

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from controller.OpenMeteoController import open_meteo_router
from controller.UtilsController import utils_router
from controller.YahooFinanceController import yahoo_finance_router
from utils.location import Location

app = FastAPI()
app.include_router(utils_router)
app.include_router(open_meteo_router)
app.include_router(yahoo_finance_router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

location = Location()
lat, lon, city = location.get_position()


@app.get("/")
async def root(request: Request):
    context = {
        "request": request,
        "message": "Hello, World!",
        "lat": lat,
        "lon": lon,
        "city": city
    }
    return templates.TemplateResponse("index.html", context)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=9111, log_level="info")
