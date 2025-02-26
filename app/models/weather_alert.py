from sqlalchemy import Column, Integer, String, ForeignKey,DATETIME
from sqlalchemy.orm import relationship
from app.db.session import Base

class WeatherAlert(Base):
    __tablename__ = "weather_alerts"

    id = Column(Integer, primary_key=True, index=True)
    msg = Column(String, nullable=False)