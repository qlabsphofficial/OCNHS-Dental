from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from typing import Optional
from models import Student, MedicalHistory
import datetime as dt

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


class StudentModel(BaseModel):
    lastname: str
    firstname: str
    middlename: Optional[str] = None
    suffix: Optional[str] = None
    dateofbirth: str
    birthplace: str
    parent_guardian_name: str
    adviser_name: str
    gender: int
    contact_no: str
    address: str
    email_address: str
    curriculum: int
    grade_level: int
    section: str
    medical_history: MedicalHistoryModel  # This is a nested model for medical history

    class Config:
        orm_mode = True



@app.post('/register_student')
async def register_student(student: StudentModel, db: Session = Depends(get_database)):
    # try:
        # Check if student already exists based on email (or any unique field)
        existing_student = db.query(Student).filter(Student.email_address == student.email_address).first()

        if not existing_student:
            # Create a new student record
            new_student = Student(
                lastname=student.lastname,
                firstname=student.firstname,
                middlename=student.middlename,
                suffix=student.suffix,
                dateofbirth=student.dateofbirth,
                birthplace=student.birthplace,
                parent_guardian_name=student.parent_guardian_name,
                adviser_name=student.adviser_name,
                gender=student.gender,
                contact_no=student.contact_no,
                address=student.address,
                email_address=student.email_address,
                curriculum=student.curriculum,
                grade_level=student.grade_level,
                section=student.section
            )

            db.add(new_student)
            db.commit()

            # Now create medical history record for the student
            new_medical_history = MedicalHistory(
                student_id=new_student.id,
                good_health=student.medical_history.good_health,
                under_medical_treatment=student.medical_history.under_medical_treatment,
                condition_being_treated=student.medical_history.condition_being_treated,
                serious_illness=student.medical_history.serious_illness,
                illness_or_operation=student.medical_history.illness_or_operation,
                hospitalized=student.medical_history.hospitalized,
                hospitalization_details=student.medical_history.hospitalization_details,
                taking_medication=student.medical_history.taking_medication,
                medication_details=student.medical_history.medication_details,
                use_tobacco=student.medical_history.use_tobacco,
                use_alcohol_or_drugs=student.medical_history.use_alcohol_or_drugs,
                pregnant_nursing_birth_control=student.medical_history.pregnant_nursing_birth_control,
                pregnant_nursing_birth_control_details=student.medical_history.pregnant_nursing_birth_control_details,
                toothbrush=student.medical_history.toothbrush,
                brush_times_per_day=student.medical_history.brush_times_per_day,
                change_toothbrush_per_year=student.medical_history.change_toothbrush_per_year,
                use_toothpaste=student.medical_history.use_toothpaste,
                dentist_visits_per_year=student.medical_history.dentist_visits_per_year,
                allergy=student.medical_history.allergy,
                allergy_details=student.medical_history.allergy_details,
                emphysema=student.medical_history.emphysema,
                bleeding_problems=student.medical_history.bleeding_problems,
                blood_diseases=student.medical_history.blood_diseases,
                head_injuries=student.medical_history.head_injuries,
                arthritis_rheumatism=student.medical_history.arthritis_rheumatism,
                high_fever=student.medical_history.high_fever,
                diabetes=student.medical_history.diabetes,
                chest_pain=student.medical_history.chest_pain,
                stroke=student.medical_history.stroke,
                cancer_tumors=student.medical_history.cancer_tumors,
                anemia=student.medical_history.anemia,
                angina=student.medical_history.angina,
                asthma=student.medical_history.asthma,
                high_blood_pressure=student.medical_history.high_blood_pressure,
                low_blood_pressure=student.medical_history.low_blood_pressure,
                aids_hiv_infection=student.medical_history.aids_hiv_infection,
                sexually_transmitted_disease=student.medical_history.sexually_transmitted_disease,
                stomach_troubles_ulcers=student.medical_history.stomach_troubles_ulcers,
                fainting_seizure=student.medical_history.fainting_seizure,
                rapid_weight_loss_radiation_therapy=student.medical_history.rapid_weight_loss_radiation_therapy,
                joint_replacement_implant=student.medical_history.joint_replacement_implant,
                heart_surgery_heart_attack=student.medical_history.heart_surgery_heart_attack,
                thyroid_problem=student.medical_history.thyroid_problem,
                heart_disease=student.medical_history.heart_disease,
                heart_murmur=student.medical_history.heart_murmur,
                hepatitis_liver_disease=student.medical_history.hepatitis_liver_disease,
                rheumatic_seizure=student.medical_history.rheumatic_seizure,
                respiratory_problems=student.medical_history.respiratory_problems,
                hepatitis_jaundice=student.medical_history.hepatitis_jaundice,
                tuberculosis=student.medical_history.tuberculosis,
                swollen_ankles=student.medical_history.swollen_ankles,
                kidney_disease=student.medical_history.kidney_disease,
                other_diseases=student.medical_history.other_diseases
            )

            db.add(new_medical_history)
            db.commit()

            return {
                'response': 'Student and Medical History registration successful.',
                'status_code': 200,
                'student_id': new_student.id,
                # 'medical_history_id': new_medical_history.id
            }
        else:
            raise HTTPException(status_code=400, detail="Student with this email already exists.")
    # except Exception as e:
    #     db.rollback()
    #     raise HTTPException(status_code=500, detail=str(e))


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
