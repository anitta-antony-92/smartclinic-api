from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token:str
    token_type:str


class DoctorBase(BaseModel):
    name: str
    specialization: str
    email: EmailStr

class DoctorCreate(DoctorBase):
    pass

class DoctorOut(DoctorBase):
    id: int

    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class PatientCreate(PatientBase):
    pass

class PatientOut(PatientBase):
    id: int

    class Config:
        orm_mode = True


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_time: datetime

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentOut(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class LabReportBase(BaseModel):
    patient_id: int
    report_type: str  # e.g., "PDF" or "Text"

class LabReportCreate(LabReportBase):
    report_text: Optional[str] = None

class LabReportOut(LabReportBase):
    id: int
    uploaded_at: datetime
    report_text: Optional[str]

    class Config:
        orm_mode = True