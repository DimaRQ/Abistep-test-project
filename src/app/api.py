from fastapi import FastAPI

from src.app.v1 import router as v1_router

app = FastAPI(prefix="/api")

app.include_router(v1_router)
