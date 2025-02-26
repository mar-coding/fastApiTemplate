import os

import aioredis
from dotenv import load_dotenv
load_dotenv("../../.env")
REDIS = aioredis.from_url("redis://default:eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81@localhost:6380", decode_responses=True)

class Settings:
    DAYS = 24 * 60


    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")

    # DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
    SECRET_KEY = os.getenv("SECRET_KEY", "sraGbRmjYQXmYdYl8Pk!OFE35UP6n/QqqpOD=iu/bUXBFSSPwnsuprP6T45Q5Ymywu2khUka!6II3Ql")
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:mypassword@0.0.0.0:5332/app")

    ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRES_MINUTES = 5
    REFRESH_TOKEN_EXPIRES_MINUTES = 1 * DAYS # 1 day


    OWM_URL = "http://api.openweathermap.org/data/2.5/weather?q=Milan,it&APPID=048f276409a861472c139e508f5879a2"

settings = Settings()