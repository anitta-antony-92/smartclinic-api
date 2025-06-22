from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import LabReport, Patient
from app.schemas import LabReportCreate, LabReportOut
from typing import List, Optional
from datetime import datetime
import shutil
import os

router = APIRouter(prefix="/lab-reports", tags=["Lab Reports"])

UPLOAD_DIR = "uploads/reports/"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LabReportOut)
async def upload_lab_report(
    patient_id: int = Form(...),
    report_type: str = Form(...),
    report_file: Optional[UploadFile] = File(None),
    report_text: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    # Validate patient exists
    if not db.query(Patient).filter(Patient.id == patient_id).first():
        raise HTTPException(status_code=404, detail="Patient not found")

    if report_type == "PDF":
        if not report_file:
            raise HTTPException(status_code=400, detail="PDF file is required")
        # Save file locally
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        file_location = os.path.join(UPLOAD_DIR, report_file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(report_file.file, buffer)

        lab_report = LabReport(patient_id=patient_id, report_type=report_type, file_path=file_location)

    elif report_type == "Text":
        if not report_text:
            raise HTTPException(status_code=400, detail="Report text is required")
        lab_report = LabReport(patient_id=patient_id, report_type=report_type, report_text=report_text)

    else:
        raise HTTPException(status_code=400, detail="Invalid report type")

    db.add(lab_report)
    db.commit()
    db.refresh(lab_report)
    return lab_report

@router.get("/patient/{patient_id}", response_model=List[LabReportOut])
def get_reports_for_patient(patient_id: int, db: Session = Depends(get_db)):
    if not db.query(Patient).filter(Patient.id == patient_id).first():
        raise HTTPException(status_code=404, detail="Patient not found")

    reports = db.query(LabReport).filter(LabReport.patient_id == patient_id).all()
    return reports
