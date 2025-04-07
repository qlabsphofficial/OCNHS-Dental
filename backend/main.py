from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from typing import Optional
from models import Student, MedicalHistory, Appointment, Admin
from datetime import date, datetime
from sqlalchemy import extract

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
    firstname: str
    middlename: Optional[str] = None
    lastname: str
    suffix: Optional[str] = None
    dateofbirth: date
    gender: str
    age: int
    birthplace: str
    contact_no: str
    address: str
    email_address: str
    password: str
    confirm_password: str

    class Config:
        orm_mode = True


class LoginModel(BaseModel):
    email_address: str
    password: str


class MedicalHistoryModel(BaseModel):
    student_id: int

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

    parent_guardian_name: Optional[str] = None
    adviser_name: Optional[str] = None
    curriculum: Optional[str] = None
    grade_level: Optional[str] = None
    section: Optional[str] = None

    class Config:
        orm_mode = True


class AppointmentModel(BaseModel):
    student_id: int
    appointment_type: str
    appointment_datetime: datetime
    status: Optional[str] = 'PENDING'

    class Config:
        orm_mode = True
    
    
class StudentUpdateModel(BaseModel):
    student_id: int
    firstname: Optional[str] = None
    middlename: Optional[str] = None
    lastname: Optional[str] = None
    suffix: Optional[str] = None
    dateofbirth: Optional[date] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    birthplace: Optional[str] = None
    contact_no: Optional[str] = None
    address: Optional[str] = None
    parent_guardian_name: Optional[str] = None
    adviser_name: Optional[str] = None
    curriculum: Optional[str] = None
    grade_level: Optional[str] = None
    section: Optional[str] = None

    class Config:
        orm_mode = True

    
class AdminRegisterModel(BaseModel):
    firstname: Optional[str] = None
    middlename: Optional[str] = None
    lastname: Optional[str] = None
    suffix: Optional[str] = None
    dateofbirth: Optional[date] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    birthplace: Optional[str] = None
    contact_number: Optional[str] = None
    address: Optional[str] = None
    email: str
    password: str
    confirm_password: str

    class Config:
        orm_mode = True

    
class AdminLoginModel(BaseModel):
    email: str
    password: str


class AppointmentFilterRequest(BaseModel):
    year: int
    month: int


class UpdateMedicalRecordRequest(BaseModel):
    student_id: int

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
    if student.password != student.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    existing_student = db.query(Student).filter(Student.email_address == student.email_address).first()
    if existing_student:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_student = Student(
        firstname=student.firstname,
        middlename=student.middlename,
        lastname=student.lastname,
        suffix=student.suffix,
        dateofbirth=student.dateofbirth,
        gender=student.gender,
        age=student.age,
        birthplace=student.birthplace,
        contact_no=student.contact_no,
        address=student.address,
        email_address=student.email_address,
        password=student.password
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {"message": "Registration successful", "status_code": 200, "new_student_id": new_student.id}

    
@app.post("/login")
async def login(login_data: LoginModel, db: Session = Depends(get_database)):
    student = db.query(Student).filter(Student.email_address == login_data.email_address).first()

    if not student or student.password != login_data.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    medical_history = db.query(MedicalHistory).filter(MedicalHistory.student_id == student.id).first()

    if medical_history:
        return {
            "message": "Login successful",
            "student_data": student,
            "medical_history_status": "exists"
        }
    else:
        return {
            "message": "Login successful",
            "student_data": student,
            "medical_history_status": "not_exists"
        }
    

@app.post("/create_medical_history")
async def create_medical_history(medical_history_data: MedicalHistoryModel, db: Session = Depends(get_database)):

    student = db.query(Student).filter(Student.id == medical_history_data.student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.parent_guardian_name = medical_history_data.parent_guardian_name
    student.adviser_name = medical_history_data.adviser_name
    student.curriculum = medical_history_data.curriculum
    student.grade_level = medical_history_data.grade_level
    student.section = medical_history_data.section

    db.commit()
    db.refresh(student)

    medical_history = db.query(MedicalHistory).filter(MedicalHistory.student_id == medical_history_data.student_id).first()

    if not medical_history:
        new_medical_history = MedicalHistory(
            student_id=medical_history_data.student_id,
            good_health=medical_history_data.good_health,
            under_medical_treatment=medical_history_data.under_medical_treatment,
            condition_being_treated=medical_history_data.condition_being_treated,
            serious_illness=medical_history_data.serious_illness,
            illness_or_operation=medical_history_data.illness_or_operation,
            hospitalized=medical_history_data.hospitalized,
            hospitalization_details=medical_history_data.hospitalization_details,
            taking_medication=medical_history_data.taking_medication,
            medication_details=medical_history_data.medication_details,
            use_tobacco=medical_history_data.use_tobacco,
            use_alcohol_or_drugs=medical_history_data.use_alcohol_or_drugs,
            pregnant_nursing_birth_control=medical_history_data.pregnant_nursing_birth_control,
            pregnant_nursing_birth_control_details=medical_history_data.pregnant_nursing_birth_control_details,
            toothbrush=medical_history_data.toothbrush,
            brush_times_per_day=medical_history_data.brush_times_per_day,
            change_toothbrush_per_year=medical_history_data.change_toothbrush_per_year,
            use_toothpaste=medical_history_data.use_toothpaste,
            dentist_visits_per_year=medical_history_data.dentist_visits_per_year,
            allergy=medical_history_data.allergy,
            allergy_details=medical_history_data.allergy_details,
            emphysema=medical_history_data.emphysema,
            bleeding_problems=medical_history_data.bleeding_problems,
            blood_diseases=medical_history_data.blood_diseases,
            head_injuries=medical_history_data.head_injuries,
            arthritis_rheumatism=medical_history_data.arthritis_rheumatism,
            high_fever=medical_history_data.high_fever,
            diabetes=medical_history_data.diabetes,
            chest_pain=medical_history_data.chest_pain,
            stroke=medical_history_data.stroke,
            cancer_tumors=medical_history_data.cancer_tumors,
            anemia=medical_history_data.anemia,
            angina=medical_history_data.angina,
            asthma=medical_history_data.asthma,
            high_blood_pressure=medical_history_data.high_blood_pressure,
            low_blood_pressure=medical_history_data.low_blood_pressure,
            aids_hiv_infection=medical_history_data.aids_hiv_infection,
            sexually_transmitted_disease=medical_history_data.sexually_transmitted_disease,
            stomach_troubles_ulcers=medical_history_data.stomach_troubles_ulcers,
            fainting_seizure=medical_history_data.fainting_seizure,
            rapid_weight_loss_radiation_therapy=medical_history_data.rapid_weight_loss_radiation_therapy,
            joint_replacement_implant=medical_history_data.joint_replacement_implant,
            heart_surgery_heart_attack=medical_history_data.heart_surgery_heart_attack,
            thyroid_problem=medical_history_data.thyroid_problem,
            heart_disease=medical_history_data.heart_disease,
            heart_murmur=medical_history_data.heart_murmur,
            hepatitis_liver_disease=medical_history_data.hepatitis_liver_disease,
            rheumatic_seizure=medical_history_data.rheumatic_seizure,
            respiratory_problems=medical_history_data.respiratory_problems,
            hepatitis_jaundice=medical_history_data.hepatitis_jaundice,
            tuberculosis=medical_history_data.tuberculosis,
            swollen_ankles=medical_history_data.swollen_ankles,
            kidney_disease=medical_history_data.kidney_disease,
            other_diseases=medical_history_data.other_diseases
        )
        db.add(new_medical_history)
        db.commit()
        db.refresh(new_medical_history)

    return {"message": "Student and medical history updated successfully"}


@app.post("/create_appointment")
async def create_appointment(appointment_data: AppointmentModel, db: Session = Depends(get_database)):
    student = db.query(Student).filter(Student.id == appointment_data.student_id).first()

    if not student:
        raise HTTPException(status_code=400, detail="Student not found")
    
    new_appointment = Appointment(
        student_id=appointment_data.student_id,
        appointment_type=appointment_data.appointment_type,
        appointment_datetime=appointment_data.appointment_datetime,
        status=appointment_data.status
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return {
        "message": "Appointment created successfully",
    }


@app.get("/get_student_appointments")
async def get_student_appointments(student_id: int, db: Session = Depends(get_database)):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    appointments = db.query(Appointment).filter(Appointment.student_id == student_id).all()
    
    if not appointments:
        return {"message": "No appointments found for this student"}
    
    return {"appointments": appointments}


@app.put("/update_student")
async def update_student(student_data: StudentUpdateModel, db: Session = Depends(get_database)):
    student = db.query(Student).filter(Student.id == student_data.student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.firstname = student_data.firstname
    student.middlename = student_data.middlename
    student.lastname = student_data.lastname
    student.suffix = student_data.suffix
    student.dateofbirth = student_data.dateofbirth
    student.gender = student_data.gender
    student.age = student_data.age
    student.birthplace = student_data.birthplace
    student.contact_no = student_data.contact_no
    student.address = student_data.address
    student.parent_guardian_name = student_data.parent_guardian_name
    student.adviser_name = student_data.adviser_name
    student.curriculum = student_data.curriculum
    student.grade_level = student_data.grade_level
    student.section = student_data.section

    db.commit()
    db.refresh(student)

    return {"message": "Student updated successfully", "student_data": student}


@app.get("/get_medical_history")
async def get_medical_history(student_id: int, db: Session = Depends(get_database)):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    medical_history = db.query(MedicalHistory).filter(MedicalHistory.student_id == student_id).all()
    
    if not medical_history:
        return {"message": "No medical history found for this student"}
    
    return {"medical_history": medical_history}


@app.post("/register_admin")
async def register_admin(admin_data: AdminRegisterModel, db: Session = Depends(get_database)):
    try:
        if admin_data.password != admin_data.confirm_password:
            raise HTTPException(status_code=400, detail="Passwords do not match")
        
        existing_admin = db.query(Admin).filter(Admin.email == admin_data.email).first()
        if existing_admin:
            raise HTTPException(status_code=400, detail="Email already registered")

        new_admin = Admin(
            firstname=admin_data.firstname,
            middlename=admin_data.middlename,
            lastname=admin_data.lastname,
            suffix=admin_data.suffix,
            dateofbirth=admin_data.dateofbirth,
            gender=admin_data.gender,
            age=admin_data.age,
            birthplace=admin_data.birthplace,
            contact_number=admin_data.contact_number,
            address=admin_data.address,
            email=admin_data.email,
            password=admin_data.password
        )

        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)

        return {"message": "Admin registration successful", "status_code": 200}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")
    

@app.post("/login_admin")
async def login_admin(login_data: AdminLoginModel, db: Session = Depends(get_database)):
    admin = db.query(Admin).filter(Admin.email == login_data.email).first()

    if not admin or admin.password != login_data.password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {
        "message": "Login successful",
        "admin_data": admin
    }


@app.get("/get_pending_appointments")
async def get_pending_appointments(db: Session = Depends(get_database)):
    results = (
        db.query(Appointment, Student)
        .join(Student, Student.id == Appointment.student_id)  # INNER JOIN
        .filter(Appointment.status == 'PENDING')
        .all()
    )

    # Format results nicely
    formatted_results = []
    for appointment, student in results:
        formatted_results.append({
        # Student fields
        "student_id": student.id if student else None,
        "firstname": student.firstname if student else None,
        "middlename": student.middlename if student else None,
        "lastname": student.lastname if student else None,
        "suffix": student.suffix if student else None,
        "dateofbirth": student.dateofbirth if student else None,
        "gender": student.gender if student else None,
        "age": student.age if student else None,
        "birthplace": student.birthplace if student else None,
        "contact_no": student.contact_no if student else None,
        "address": student.address if student else None,
        "email_address": student.email_address if student else None,
        "password": student.password if student else None,
        "parent_guardian_name": student.parent_guardian_name if student else None,
        "adviser_name": student.adviser_name if student else None,
        "curriculum": student.curriculum if student else None,
        "grade_level": student.grade_level if student else None,
        "section": student.section if student else None,

        # Appointment fields
        "appointment_id": appointment.id,
        "appointment_type": appointment.appointment_type,
        "appointment_datetime": appointment.appointment_datetime,
        "status": appointment.status,
    })

    return {"pending_appointments": formatted_results}


@app.post("/appointments_by_month") 
async def get_appointments_by_month(filter: AppointmentFilterRequest, db: Session = Depends(get_database)):
    year = filter.year
    month = filter.month
    
    # Query appointments with the extracted year and month
    results = (
        db.query(Appointment, Student)
        .join(Student, Student.id == Appointment.student_id)  # INNER JOIN to ensure only matching students
        .filter(
            extract('year', Appointment.appointment_datetime) == year,
            extract('month', Appointment.appointment_datetime) == month
        )
        .all()
    )
    
    if not results:
        raise HTTPException(status_code=404, detail="No appointments found for the given month and year")
    
    formatted_results = []
    for appointment, student in results:
        formatted_results.append({
            # Student fields
        "student_id": student.id if student else None,
        "firstname": student.firstname if student else None,
        "middlename": student.middlename if student else None,
        "lastname": student.lastname if student else None,
        "suffix": student.suffix if student else None,
        "dateofbirth": student.dateofbirth if student else None,
        "gender": student.gender if student else None,
        "age": student.age if student else None,
        "birthplace": student.birthplace if student else None,
        "contact_no": student.contact_no if student else None,
        "address": student.address if student else None,
        "email_address": student.email_address if student else None,
        "password": student.password if student else None,
        "parent_guardian_name": student.parent_guardian_name if student else None,
        "adviser_name": student.adviser_name if student else None,
        "curriculum": student.curriculum if student else None,
        "grade_level": student.grade_level if student else None,
        "section": student.section if student else None,

        # Appointment fields
        "appointment_id": appointment.id,
        "appointment_type": appointment.appointment_type,
        "appointment_datetime": appointment.appointment_datetime,
        "status": appointment.status,
        })

    return {"appointments": formatted_results}


@app.get("/get_all_appointments")
async def get_all_appointments(db: Session = Depends(get_database)):
    appointments = db.query(Appointment).all()
    
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found")
    
    formatted_appointments = []
    for appointment in appointments:
        formatted_appointments.append({
            "appointment_id": appointment.id,
            "student_id": appointment.student_id,
            "appointment_type": appointment.appointment_type,
            "appointment_datetime": appointment.appointment_datetime,
            "status": appointment.status,
        })
    
    return {"appointments": formatted_appointments}


@app.post("/update_medical_record")
async def update_medical_record(medical_history_data: UpdateMedicalRecordRequest, db: Session = Depends(get_database)):
    # Check if the student exists
    student = db.query(Student).filter(Student.id == medical_history_data.student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    medical_history = db.query(MedicalHistory).filter(MedicalHistory.student_id == medical_history_data.student_id).first()
    
    if not medical_history:
        raise HTTPException(status_code=404, detail="Medical record not found for the student")

    else:
        medical_history.good_health = medical_history_data.good_health
        medical_history.under_medical_treatment = medical_history_data.under_medical_treatment
        medical_history.condition_being_treated = medical_history_data.condition_being_treated
        medical_history.serious_illness = medical_history_data.serious_illness
        medical_history.illness_or_operation = medical_history_data.illness_or_operation
        medical_history.hospitalized = medical_history_data.hospitalized
        medical_history.hospitalization_details = medical_history_data.hospitalization_details
        medical_history.taking_medication = medical_history_data.taking_medication
        medical_history.medication_details = medical_history_data.medication_details
        medical_history.use_tobacco = medical_history_data.use_tobacco
        medical_history.use_alcohol_or_drugs = medical_history_data.use_alcohol_or_drugs
        medical_history.pregnant_nursing_birth_control = medical_history_data.pregnant_nursing_birth_control
        medical_history.pregnant_nursing_birth_control_details = medical_history_data.pregnant_nursing_birth_control_details
        medical_history.toothbrush = medical_history_data.toothbrush
        medical_history.brush_times_per_day = medical_history_data.brush_times_per_day
        medical_history.change_toothbrush_per_year = medical_history_data.change_toothbrush_per_year
        medical_history.use_toothpaste = medical_history_data.use_toothpaste
        medical_history.dentist_visits_per_year = medical_history_data.dentist_visits_per_year
        medical_history.allergy = medical_history_data.allergy
        medical_history.allergy_details = medical_history_data.allergy_details
        medical_history.emphysema = medical_history_data.emphysema
        medical_history.bleeding_problems = medical_history_data.bleeding_problems
        medical_history.blood_diseases = medical_history_data.blood_diseases
        medical_history.head_injuries = medical_history_data.head_injuries
        medical_history.arthritis_rheumatism = medical_history_data.arthritis_rheumatism
        medical_history.high_fever = medical_history_data.high_fever
        medical_history.diabetes = medical_history_data.diabetes
        medical_history.chest_pain = medical_history_data.chest_pain
        medical_history.stroke = medical_history_data.stroke
        medical_history.cancer_tumors = medical_history_data.cancer_tumors
        medical_history.anemia = medical_history_data.anemia
        medical_history.angina = medical_history_data.angina
        medical_history.asthma = medical_history_data.asthma
        medical_history.high_blood_pressure = medical_history_data.high_blood_pressure
        medical_history.low_blood_pressure = medical_history_data.low_blood_pressure
        medical_history.aids_hiv_infection = medical_history_data.aids_hiv_infection
        medical_history.sexually_transmitted_disease = medical_history_data.sexually_transmitted_disease
        medical_history.stomach_troubles_ulcers = medical_history_data.stomach_troubles_ulcers
        medical_history.fainting_seizure = medical_history_data.fainting_seizure
        medical_history.rapid_weight_loss_radiation_therapy = medical_history_data.rapid_weight_loss_radiation_therapy
        medical_history.joint_replacement_implant = medical_history_data.joint_replacement_implant
        medical_history.heart_surgery_heart_attack = medical_history_data.heart_surgery_heart_attack
        medical_history.thyroid_problem = medical_history_data.thyroid_problem
        medical_history.heart_disease = medical_history_data.heart_disease
        medical_history.heart_murmur = medical_history_data.heart_murmur
        medical_history.hepatitis_liver_disease = medical_history_data.hepatitis_liver_disease
        medical_history.rheumatic_seizure = medical_history_data.rheumatic_seizure
        medical_history.respiratory_problems = medical_history_data.respiratory_problems
        medical_history.hepatitis_jaundice = medical_history_data.hepatitis_jaundice
        medical_history.tuberculosis = medical_history_data.tuberculosis
        medical_history.swollen_ankles = medical_history_data.swollen_ankles
        medical_history.kidney_disease = medical_history_data.kidney_disease
        medical_history.other_diseases = medical_history_data.other_diseases
        
        db.commit()
        db.refresh(medical_history)

        return {"message": "Medical history updated successfully", "medical_history": medical_history}
