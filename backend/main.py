from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from typing import Optional
from models import Student, MedicalHistory
from datetime import date

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

def get_database():
    db = None

    try:
        db = SessionLocal()
    finally:
        yield db
        db.close()


class StudentModel(BaseModel):
    lastname: str
    firstname: str
    middlename: Optional[str] = None
    suffix: Optional[str] = None
    dateofbirth: date  # Changed to date type
    gender: int
    birthplace: str
    contact_no: str
    address: str
    email_address: str
    password: str  # Added password field

    class Config:
        orm_mode = True


class MedicalHistoryModel(BaseModel):
    good_health: Optional[int] = None
    under_medical_treatment: Optional[int] = None
    condition_being_treated: Optional[str] = None
    serious_illness: Optional[int] = None
    illness_or_operation: Optional[str] = None
    hospitalized: Optional[int] = None
    hospitalization_details: Optional[str] = None
    taking_medication: Optional[int] = None
    medication_details: Optional[str] = None
    use_tobacco: Optional[int] = None
    use_alcohol_or_drugs: Optional[int] = None
    pregnant_nursing_birth_control: Optional[int] = None
    pregnant_nursing_birth_control_details: Optional[str] = None
    toothbrush: Optional[int] = None
    brush_times_per_day: Optional[int] = None
    change_toothbrush_per_year: Optional[int] = None
    use_toothpaste: Optional[int] = None
    dentist_visits_per_year: Optional[int] = None

    allergy: Optional[int] = None
    allergy_details: Optional[str] = None
    emphysema: Optional[int] = None
    bleeding_problems: Optional[int] = None
    blood_diseases: Optional[int] = None
    head_injuries: Optional[int] = None
    arthritis_rheumatism: Optional[int] = None
    high_fever: Optional[int] = None
    diabetes: Optional[int] = None
    chest_pain: Optional[int] = None
    stroke: Optional[int] = None
    cancer_tumors: Optional[int] = None
    anemia: Optional[int] = None
    angina: Optional[int] = None
    asthma: Optional[int] = None
    high_blood_pressure: Optional[int] = None
    low_blood_pressure: Optional[int] = None
    aids_hiv_infection: Optional[int] = None
    sexually_transmitted_disease: Optional[int] = None
    stomach_troubles_ulcers: Optional[int] = None
    fainting_seizure: Optional[int] = None
    rapid_weight_loss_radiation_therapy: Optional[int] = None
    joint_replacement_implant: Optional[int] = None
    heart_surgery_heart_attack: Optional[int] = None
    thyroid_problem: Optional[int] = None
    heart_disease: Optional[int] = None
    heart_murmur: Optional[int] = None
    hepatitis_liver_disease: Optional[int] = None
    rheumatic_seizure: Optional[int] = None
    respiratory_problems: Optional[int] = None
    hepatitis_jaundice: Optional[int] = None
    tuberculosis: Optional[int] = None
    swollen_ankles: Optional[int] = None
    kidney_disease: Optional[int] = None
    other_diseases: Optional[str] = None

    class Config:
        orm_mode = True

@app.post("/register")
async def register(student: StudentModel, db: Session = Depends(get_database)):
    # try:
        # Check if email already exists
        existing_student = db.query(Student).filter(Student.email_address == student.email_address).first()
        if existing_student:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Create a new student object
        new_student = Student(
            firstname=student.firstname,
            middlename=student.middlename,
            lastname=student.lastname,
            suffix=student.suffix,
            dateofbirth=student.dateofbirth,
            gender=student.gender,
            birthplace=student.birthplace,
            contact_no=student.contact_no,
            address=student.address,
            email_address=student.email_address,
            password=student.password
        )

        # Add the student to the database
        db.add(new_student)
        db.commit()

        return {"message": "Registration successful", "status_code": 200, "new_student_id": new_student.id}

    # except Exception as e:
    #     db.rollback()  # Rollback in case of error
    #     raise HTTPException(status_code=500, detail="Registration failed")


# @app.post('/login')
# async def login(username: str, password: str, db: Session = Depends(get_database)):
#     try:
#         existing_user = db.query(User).filter(User.username == username).first()

#         if existing_user:
#             if existing_user.password == password:
#                 return { 'response': 'Login successful.', 'user_data': existing_user, 'status_code': 200 }
#             else:
#                 return { 'response': 'Login failed.', 'status_code': 403 }
#     except:
#         return { 'response': 'Login failed.', 'status_code': 403 }
