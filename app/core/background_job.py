from http.client import responses

import aioredis
from celery import Celery
import requests
from app.models.location import Location
from app.models.weather_data import WeatherData
from app.db.session import SessionLocal
from app.core.config import settings

celery_app = Celery(__name__, broker="redis://default:eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81@localhost:6380/0")

@celery_app.task
def fetch_weather_data(city_name: str = "milan"):
    session = SessionLocal()

    response = requests.get(settings.WEATHER_API_URL)
    if response.status_code == 200:
        data = response.json()
        location = session.query(Location).filter(Location.name == city_name).first()
        if not location:
            location = Location(name=city_name,lot=data["coord"]["lon"],lat=data["coord"]["lat"])
            session.add(location)
            session.commit()
        weather_data = WeatherData(temp=data["main"]["temp"],humadity=data["main"]["humidity"],
                                   location_id=location.id,wind=data["wind"]["speed"],pressure=data["main"]["pressure"],
                                   discription= data["weather"][0]["description"])
        session.add(weather_data)
        session.commit()

        redis = aioredis.from_url("://default:eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81@localhost:6380/0", decode_responses=True)
        redis.set(f"weather:{city_name}", str(weather_data),ex=740) # every 14 mins
    session.close()