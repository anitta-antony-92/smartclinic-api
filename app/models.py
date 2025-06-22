from sqlalchemy import Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Doctor(Base):
    __tablename__ = "doctors"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)



class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Optional: relationships for joining later
    patient = relationship("Patient")
    doctor = relationship("Doctor")


class LabReport(Base):
    __tablename__ = "lab_reports"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    report_type = Column(String, nullable=False)  # e.g. "PDF" or "Text"
    file_path = Column(String, nullable=True)     # For saved files (optional)
    report_text = Column(String, nullable=True)   # For text content
    # uploaded_at = Column(DateTime, default=datetime.utcnow)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    patient = relationship("Patient")