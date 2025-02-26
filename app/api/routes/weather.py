from fastapi import APIRouter 
from sqlalchemy.orm import Session

from app.core.background_job import fetch_weather_data
from app.db.session import DatabaseSession 
from app.models.location import Location
from app.core.config import REDIS as redis

router = APIRouter()


@router.get("/weather/{city_name}")
async def get_weather(city_name: str, db: Session = DatabaseSession):
    cached_weather = await redis.get(f"weather:{city_name}")
    if cached_weather:
        return {"source": "cache", "data": eval(cached_weather)}
    db_location = db.query(Location).filter(Location.name == city_name).first()
    if db_location and db_location.weather_data:
        return {"source": "db", "data": db_location.weather_data.as_dict()}

    fetch_weather_data.delay("milan")
    return {"message": "try it later."}

@router.get("weather/alerts/{city_name}")
async def get_weather_alerts(city_name: str, db: Session = DatabaseSession):
    location = db.query(Location).filter(Location.name == city_name).first()
    if not location or location.weather_data is None:
        return {"message": "No weather data found for this city."}

    fresh_data = location.weather_data.as_dict()
    alerts = []

    if fresh_data.pressure < 1000 :
        alerts.append("possible storm  ")

    return {"city": city_name, "alerts": alerts}