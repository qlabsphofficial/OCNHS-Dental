from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # assuming you have a Base = declarative_base()

# --- Students Table ---
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    firstname = Column(String, nullable=True, default=None)
    middlename = Column(String, nullable=True, default=None)
    lastname = Column(String, nullable=True, default=None)
    suffix = Column(String, nullable=True, default=None)
    dateofbirth = Column(Date, nullable=True, default=None)  # Changed to Date type
    gender = Column(Integer, nullable=True, default=None)  # will use index values
    birthplace = Column(String, nullable=True, default=None)
    contact_no = Column(String, nullable=True, default=None)
    address = Column(String, nullable=True, default=None)
    email_address = Column(String, nullable=True, default=None)
    password = Column(String, nullable=False, default=None)  # Added password column with nullable=False
    
    parent_guardian_name = Column(String, nullable=True, default=None)
    adviser_name = Column(String, nullable=True, default=None)
    curriculum = Column(Integer, nullable=True, default=None)  # will use index values
    grade_level = Column(Integer, nullable=True, default=None)  # will use index values
    section = Column(String, nullable=True, default=None)

    medical_history = relationship('MedicalHistory', back_populates='student')


# --- Medical History Table ---
class MedicalHistory(Base):
    __tablename__ = 'medical_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=True)

    good_health = Column(Integer, nullable=True, default=None)
    under_medical_treatment = Column(Integer, nullable=True, default=None)
    condition_being_treated = Column(String, nullable=True,     default=None)
    serious_illness = Column(Integer, nullable=True, default=None)
    illness_or_operation = Column(String, nullable=True, default=None)
    hospitalized = Column(Integer, nullable=True, default=None)
    hospitalization_details = Column(String, nullable=True, default=None)
    taking_medication = Column(Integer, nullable=True, default=None)
    medication_details = Column(String, nullable=True, default=None)
    use_tobacco = Column(Integer, nullable=True, default=None)
    use_alcohol_or_drugs = Column(Integer, nullable=True, default=None)
    pregnant_nursing_birth_control = Column(Integer, nullable=True, default=None)
    pregnant_nursing_birth_control_details = Column(String, nullable=True, default=None)
    toothbrush = Column(Integer, nullable=True, default=None)
    brush_times_per_day = Column(Integer, nullable=True, default=None)
    change_toothbrush_per_year = Column(Integer, nullable=True, default=None)
    use_toothpaste = Column(Integer, nullable=True, default=None)
    dentist_visits_per_year = Column(Integer, nullable=True, default=None)

    allergy = Column(Integer, nullable=True, default=None)
    allergy_details = Column(String, nullable=True, default=None)
    emphysema = Column(Integer, nullable=True, default=None)
    bleeding_problems = Column(Integer, nullable=True, default=None)
    blood_diseases = Column(Integer, nullable=True, default=None)
    head_injuries = Column(Integer, nullable=True, default=None)
    arthritis_rheumatism = Column(Integer, nullable=True, default=None)
    high_fever = Column(Integer, nullable=True, default=None)
    diabetes = Column(Integer, nullable=True, default=None)
    chest_pain = Column(Integer, nullable=True, default=None)
    stroke = Column(Integer, nullable=True, default=None)
    cancer_tumors = Column(Integer, nullable=True, default=None)
    anemia = Column(Integer, nullable=True, default=None)
    angina = Column(Integer, nullable=True, default=None)
    asthma = Column(Integer, nullable=True, default=None)
    high_blood_pressure = Column(Integer, nullable=True, default=None)
    low_blood_pressure = Column(Integer, nullable=True, default=None)
    aids_hiv_infection = Column(Integer, nullable=True, default=None)
    sexually_transmitted_disease = Column(Integer, nullable=True, default=None)
    stomach_troubles_ulcers = Column(Integer, nullable=True, default=None)
    fainting_seizure = Column(Integer, nullable=True, default=None)
    rapid_weight_loss_radiation_therapy = Column(Integer, nullable=True, default=None)
    joint_replacement_implant = Column(Integer, nullable=True, default=None)
    heart_surgery_heart_attack = Column(Integer, nullable=True, default=None)
    thyroid_problem = Column(Integer, nullable=True, default=None)
    heart_disease = Column(Integer, nullable=True, default=None)
    heart_murmur = Column(Integer, nullable=True, default=None)
    hepatitis_liver_disease = Column(Integer, nullable=True, default=None)
    rheumatic_seizure = Column(Integer, nullable=True, default=None)
    respiratory_problems = Column(Integer, nullable=True, default=None)
    hepatitis_jaundice = Column(Integer, nullable=True, default=None)
    tuberculosis = Column(Integer, nullable=True, default=None)
    swollen_ankles = Column(Integer, nullable=True, default=None)
    kidney_disease = Column(Integer, nullable=True, default=None)
    other_diseases = Column(String, nullable=True, default=None)

    student = relationship('Student', back_populates='medical_history')
