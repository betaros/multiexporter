from datetime import datetime
from fastapi import APIRouter, Response
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.service.YahooFinanceService import YahooFinanceService

yahoo_finance_router = APIRouter(prefix="/yahoo-finance", tags=["finance"])
yahoo_finance_service = YahooFinanceService()
scheduler = AsyncIOScheduler()


@yahoo_finance_router.on_event("startup")
async def start_scheduler():
    """
    Start the scheduler
    :return:
    """
    scheduler.add_job(yahoo_finance_service.fetch_financial_data, "interval", minutes=5, next_run_time=datetime.now())
    scheduler.start()


@yahoo_finance_router.get("/metrics", description="Return metrics for given stocks")
async def get_financial_metrics():
    """
    Get the stock data
    :return:
    """
    return Response(content=yahoo_finance_service.financial_data, media_type="text/plain")
