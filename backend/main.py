from fastapi import FastAPI
from .routers.main import api_router
from .db import engine, Base

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(api_router)