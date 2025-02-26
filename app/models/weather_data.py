from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Table
from sqlalchemy.orm import relationship
from app.db.session import Base


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    storm_warnings = Column(String, nullable=False)
    temp = Column(Float, nullable=False)
    humadity = Column(Float, nullable=False)
    wind = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    discription = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False,default=datetime.now())

    location_id = Column(Integer, ForeignKey("locations.id"))
    location = relationship("Location", back_populates="weather_data")
    alert = relationship("WeatherAlert", secondary="weather_data_alerts")

    weather_data_alerts = Table (
        "weather_data_alerts",
        Base.metadata,
        Column("weather_data_id", Integer, ForeignKey("weather_data.id")),
        Column("weather_alert_id", Integer, ForeignKey("weather_alerts.id"))
    )