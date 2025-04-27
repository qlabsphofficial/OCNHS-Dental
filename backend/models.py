from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    firstname = Column(String, nullable=True, default=None)
    middlename = Column(String, nullable=True, default=None)
    lastname = Column(String, nullable=True, default=None)
    suffix = Column(String, nullable=True, default=None)
    dateofbirth = Column(Date, nullable=True, default=None)
    gender = Column(String, nullable=True, default=None)
    age = Column(Integer, nullable=True, default=None)
    birthplace = Column(String, nullable=True, default=None)
    contact_no = Column(String, nullable=True, default=None)
    address = Column(String, nullable=True, default=None)
    email_address = Column(String, nullable=True, default=None)
    password = Column(String, nullable=False, default=None)
    
    parent_guardian_name = Column(String, nullable=True, default=None)
    adviser_name = Column(String, nullable=True, default=None)
    curriculum = Column(String, nullable=True, default=None)
    grade_level = Column(String, nullable=True, default=None)
    section = Column(String, nullable=True, default=None)

    is_archive = Column(Boolean, nullable=False, default=False)
    is_active = Column(Boolean, nullable=False, default=True)
    date_archived = Column(Date, nullable=True, default=None)

    medical_history = relationship('MedicalHistory', back_populates='student')
    appointments = relationship('Appointment', back_populates='student')
    oral_health_condition = relationship("OralHealthCondition", back_populates="student")
    temporary_teeth = relationship("TemporaryTeeth", back_populates="student")
    permanent_teeth = relationship("PermanentTeeth", back_populates="student")
    dental_procedures = relationship("DentalProcedure", back_populates="student")
    condition_treatment_needs = relationship("ConditionTreatmentNeeds", back_populates="student")



# --- Medical History Table ---
class MedicalHistory(Base):
    __tablename__ = 'medical_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=True)

    good_health = Column(Boolean, nullable=True, default=None)
    under_medical_treatment = Column(Boolean, nullable=True, default=None)
    condition_being_treated = Column(String, nullable=True, default=None)
    serious_illness = Column(Boolean, nullable=True, default=None)
    illness_or_operation = Column(String, nullable=True, default=None)
    hospitalized = Column(Boolean, nullable=True, default=None)
    hospitalization_details = Column(String, nullable=True, default=None)
    taking_medication = Column(Boolean, nullable=True, default=None)
    medication_details = Column(String, nullable=True, default=None)
    use_tobacco = Column(Boolean, nullable=True, default=None)
    use_alcohol_or_drugs = Column(Boolean, nullable=True, default=None)
    pregnant_nursing_birth_control = Column(Boolean, nullable=True, default=None)
    pregnant_nursing_birth_control_details = Column(String, nullable=True, default=None)
    toothbrush = Column(Boolean, nullable=True, default=None)
    brush_times_per_day = Column(Integer, nullable=True, default=None)
    change_toothbrush_per_year = Column(Integer, nullable=True, default=None)
    use_toothpaste = Column(Boolean, nullable=True, default=None)
    dentist_visits_per_year = Column(Integer, nullable=True, default=None)

    allergy = Column(Boolean, nullable=True, default=None)
    allergy_details = Column(String, nullable=True, default=None)
    emphysema = Column(Boolean, nullable=True, default=None)
    bleeding_problems = Column(Boolean, nullable=True, default=None)
    blood_diseases = Column(Boolean, nullable=True, default=None)
    head_injuries = Column(Boolean, nullable=True, default=None)
    arthritis_rheumatism = Column(Boolean, nullable=True, default=None)
    high_fever = Column(Boolean, nullable=True, default=None)
    diabetes = Column(Boolean, nullable=True, default=None)
    chest_pain = Column(Boolean, nullable=True, default=None)
    stroke = Column(Boolean, nullable=True, default=None)
    cancer_tumors = Column(Boolean, nullable=True, default=None)
    anemia = Column(Boolean, nullable=True, default=None)
    angina = Column(Boolean, nullable=True, default=None)
    asthma = Column(Boolean, nullable=True, default=None)
    high_blood_pressure = Column(Boolean, nullable=True, default=None)
    low_blood_pressure = Column(Boolean, nullable=True, default=None)
    aids_hiv_infection = Column(Boolean, nullable=True, default=None)
    sexually_transmitted_disease = Column(Boolean, nullable=True, default=None)
    stomach_troubles_ulcers = Column(Boolean, nullable=True, default=None)
    fainting_seizure = Column(Boolean, nullable=True, default=None)
    rapid_weight_loss_radiation_therapy = Column(Boolean, nullable=True, default=None)
    joint_replacement_implant = Column(Boolean, nullable=True, default=None)
    heart_surgery_heart_attack = Column(Boolean, nullable=True, default=None)
    thyroid_problem = Column(Boolean, nullable=True, default=None)
    heart_disease = Column(Boolean, nullable=True, default=None)
    heart_murmur = Column(Boolean, nullable=True, default=None)
    hepatitis_liver_disease = Column(Boolean, nullable=True, default=None)
    rheumatic_seizure = Column(Boolean, nullable=True, default=None)
    respiratory_problems = Column(Boolean, nullable=True, default=None)
    hepatitis_jaundice = Column(Boolean, nullable=True, default=None)
    tuberculosis = Column(Boolean, nullable=True, default=None)
    swollen_ankles = Column(Boolean, nullable=True, default=None)
    kidney_disease = Column(Boolean, nullable=True, default=None)
    other_diseases = Column(String, nullable=True, default=None)

    student = relationship('Student', back_populates='medical_history')
    

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=True)
    appointment_type = Column(String, nullable=True)
    appointment_datetime = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default='PENDING')

    student = relationship('Student', back_populates='appointments')


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=True, default=None)
    middlename = Column(String, nullable=True, default=None)
    lastname = Column(String, nullable=True, default=None)
    suffix = Column(String, nullable=True, default=None)
    dateofbirth = Column(Date, nullable=True, default=None)
    gender = Column(String, nullable=True, default=None)
    age = Column(Integer, nullable=True, default=None)
    birthplace = Column(String, nullable=True, default=None)
    contact_number = Column(String, nullable=True, default=None)
    address = Column(String, nullable=True, default=None)
    email = Column(String, nullable=True, default=None)
    password = Column(String, nullable=False)
    
    
class OralHealthCondition(Base):
    __tablename__ = "oral_health_condition"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    grade_level = Column(String, nullable=True)
    gingivitis = Column(Boolean, nullable=True, default=None)
    periodontal_disease = Column(Boolean, nullable=True, default=None)
    malocclusion = Column(Boolean, nullable=True, default=None)
    supernumerary_teeth = Column(Boolean, nullable=True, default=None)
    retained_deciduous_teeth = Column(Boolean, nullable=True, default=None)
    decubital_ulcer = Column(Boolean, nullable=True, default=None)
    calculus = Column(Boolean, nullable=True, default=None)
    cleft_lip_palate = Column(Boolean, nullable=True, default=None)
    root_fragment = Column(Boolean, nullable=True, default=None)
    fluorosis = Column(Boolean, nullable=True, default=None)
    others = Column(String, nullable=True)

    student = relationship("Student", back_populates="oral_health_condition")
    
    
class TemporaryTeeth(Base):
    __tablename__ = 'temporary_teeth'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    grade_level = Column(String, nullable=True)
    no_t_decayed = Column(Integer, nullable=True)
    no_t_filled = Column(Integer, nullable=True)
    total_dft = Column(Integer, nullable=True)

    # Relationship to Student model
    student = relationship("Student", back_populates="temporary_teeth")
    
    
class PermanentTeeth(Base):
    __tablename__ = "permanent_teeth"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    grade_level = Column(String, nullable=True)
    no_t_decayed = Column(Integer, nullable=True)
    no_t_missing = Column(Integer, nullable=True)
    no_t_filled = Column(Integer, nullable=True)
    total_d_m_f_t = Column(Integer, nullable=True)
    total_sound_teeth = Column(Integer, nullable=True)

    student = relationship("Student", back_populates="permanent_teeth")
    
    
class DentalProcedure(Base):
    __tablename__ = "dental_procedures"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    grade_level = Column(String, nullable=True)
    date = Column(Date, nullable=True)
    examination = Column(Boolean, nullable=True)
    sealant_gi = Column(Boolean, nullable=True)
    gum_treatment = Column(Boolean, nullable=True)
    permanent_filling = Column(Boolean, nullable=True)
    art = Column(Boolean, nullable=True)
    extraction = Column(Boolean, nullable=True)
    oral_prophylaxis = Column(Boolean, nullable=True)
    referral = Column(Boolean, nullable=True)
    other_oral_treatment = Column(Boolean, nullable=True)
    remarks = Column(String, nullable=True)
    examined_by = Column(String, nullable=True)

    student = relationship("Student", back_populates="dental_procedures")
    
    
class ConditionTreatmentNeeds(Base):
    __tablename__ = "condition_treatment_needs"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    tooth_number = Column(String, nullable=False)
    tooth_side = Column(String, nullable=False)
    condition = Column(String, nullable=False)
    treatment_needs = Column(String, nullable=False)

    student = relationship("Student", back_populates="condition_treatment_needs")