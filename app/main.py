from fastapi import FastAPI
from app.config import settings
from app.routes import auth
from app.routes import doctors
from app.routes import patients
from app.routes import appointments
from app.routes import lab_reports

app = FastAPI(title=settings.APP_NAME)

# Include routes
app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(patients.router)
app.include_router(appointments.router)
app.include_router(lab_reports.router)

# Health check / root endpoint
@app.get("/")
def read_root():
    return {"message" : f"Welcome to {settings.APP_NAME}"}