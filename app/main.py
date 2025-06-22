from fastapi import FastAPI
from app.config import settings
from app.routes import auth

app = FastAPI(title=settings.APP_NAME)

# Include routes
app.include_router(auth.router)

# Health check / root endpoint
@app.get("/")
def read_root():
    return {"message" : f"Welcome to {settings.APP_NAME}"}