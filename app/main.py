from fastapi import FastAPI
from app.config import settings


app = FastAPI(title=settings.APP_NAME)

@app.get("/")
def read_root():
    return {"message" : f"Welcome to {settings.APP_NAME}"}