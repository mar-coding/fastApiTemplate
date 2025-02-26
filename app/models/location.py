from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship
from app.db.session import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    lot = Column(Float, nullable=False)
    lat = Column(Float, nullable=False)
    weather_data = relationship("WeatherData", back_populates="location")
