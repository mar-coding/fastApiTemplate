from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes import weather
from app.db.session import engine
from app.db.base import Base
from fastapi.openapi.utils import get_openapi

def create_tables():
    Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    create_tables()
    yield
    print("Shutting down...")

app = FastAPI(title="FastAPI Notes API", version="1.0", lifespan=lifespan)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="FastAPI Notes API",
        version="1.0",
        description="An API for managing notes with JWT authentication",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            if "security" in openapi_schema["paths"][path][method]:
                openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.include_router(weather.router, prefix="/notes", tags=["Notes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Notes API"}