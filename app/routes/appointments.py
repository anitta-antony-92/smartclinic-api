from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Appointment, Patient, Doctor
from app.schemas import AppointmentCreate, AppointmentOut
from typing import List
from datetime import datetime

router = APIRouter(prefix="/appointments", tags=["Appointments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AppointmentOut)
def book_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    # Ensure patient and doctor exist
    if not db.query(Patient).filter(Patient.id == appointment.patient_id).first():
        raise HTTPException(status_code=404, detail="Patient not found")
    if not db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first():
        raise HTTPException(status_code=404, detail="Doctor not found")

    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

@router.get("/", response_model=List[AppointmentOut])
def list_appointments(
    date: datetime = Query(None),
    doctor_id: int = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Appointment)
    if date:
        query = query.filter(Appointment.appointment_time.date() == date.date())
    if doctor_id:
        query = query.filter(Appointment.doctor_id == doctor_id)
    return query.all()

@router.put("/{appointment_id}", response_model=AppointmentOut)
def reschedule_appointment(appointment_id: int, new_time: datetime, db: Session = Depends(get_db)):
    appt = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appt.appointment_time = new_time
    db.commit()
    db.refresh(appt)
    return appt

@router.delete("/{appointment_id}")
def cancel_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appt = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(appt)
    db.commit()
    return {"message": "Appointment canceled"}
