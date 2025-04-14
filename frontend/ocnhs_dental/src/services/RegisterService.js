import current_address from "@/address";

export async function register({
        firstName,
        middleName,
        lastName,
        suffix,
        birthDate,
        gender,
        age,
        placeOfBirth,
        contact,
        address,
        email,
        password,
        confirmPassword,
        parentName,
        adviserName,
        curriculum,
        gradeLvl,
        section,
        goodHealth,
        underMedicalTreatment,
        treatmentCondition,
        seriousIllness,
        illnessOrOperation,
        hospitalized,
        hospitalizationDetails,
        takingMedications,
        medicationsDetails,
        tobaccoUsage,
        drugUse,
        womenOnly,
        womenCondition,
        hasToothbrush,
        brushingTimes,
        toothbrushChange,
        useToothpaste,
        dentistVisits,
        allergy,
        emphysema,
        bleedingProblems,
        bloodDiseases,
        headInjuries,
        arthritis,
        highFever,
        diabetes,
        chestPain,
        stroke,
        cancer,
        anemia,
        angina,
        asthma,
        highBloodPressure,
        lowBloodPressure,
        aidsHiv,
        std,
        stomachTroubles,
        faintingSeizure,
        rapidWeightLossRadtionTherapy,
        jointReplacement,
        heartSurgery,
        thyroidProblem,
        heartDisease,
        heartMurmur,
        hepatitisLiverDisease,
        rheumaticSeizure,
        respiratoryProblems,
        hepatitisJaundice,
        tuberculosis,
        swollenAnkles,
        kidneyDisease,
        others,
    }) {
      let registerSuccessful = false;
      
      
      try {
        const response = await fetch(`${current_address}/register`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              "firstname": firstName,
              "middlename": middleName,
              "lastname": lastName,
              "suffix": suffix,
              "dateofbirth": birthDate,
              "gender": gender,
              "age": age,
              "birthplace": placeOfBirth,
              "contact_no": contact,
              "address": address,
              "email_address": email,
              "password": password,
              "confirm_password": confirmPassword,
              "parent_guardian_name": parentName,
              "adviser_name": adviserName,
              "curriculum": curriculum,
              "grade_level": gradeLvl,
              "section": section,

              
              "good_health": goodHealth,
              "under_medical_treatment": underMedicalTreatment,
              "condition_being_treated": treatmentCondition,
              "serious_illness": seriousIllness,
              "illness_or_operation": illnessOrOperation,
              "hospitalized": hospitalized,
              "hospitalization_details": hospitalizationDetails,
              "taking_medication": takingMedications,
              "medication_details": medicationsDetails,
              "use_tobacco": tobaccoUsage,
              "use_alcohol_or_drugs": drugUse,
              "pregnant_nursing_birth_control": womenOnly,
              "pregnant_nursing_birth_control_details": womenCondition,
              "toothbrush": hasToothbrush,
              "brush_times_per_day": brushingTimes,
              "change_toothbrush_per_year": toothbrushChange,
              "use_toothpaste": useToothpaste,
              "dentist_visits_per_year": dentistVisits,
              "allergy": allergy,
              "allergy_details": allergy,
              "emphysema": emphysema,
              "bleeding_problems": bleedingProblems,
              "blood_diseases": bloodDiseases,
              "head_injuries": headInjuries,
              "arthritis_rheumatism": arthritis,
              "high_fever": highFever,
              "diabetes": diabetes,
              "chest_pain": chestPain,
              "stroke": stroke,
              "cancer_tumors": cancer,
              "anemia": anemia,
              "angina": angina,
              "asthma": asthma,
              "high_blood_pressure": highBloodPressure,
              "low_blood_pressure": lowBloodPressure,
              "aids_hiv_infection": aidsHiv,
              "sexually_transmitted_disease": std,
              "stomach_troubles_ulcers": stomachTroubles,
              "fainting_seizure": faintingSeizure,
              "rapid_weight_loss_radiation_therapy": rapidWeightLossRadtionTherapy,
              "joint_replacement_implant": jointReplacement,
              "heart_surgery_heart_attack": heartSurgery,
              "thyroid_problem": thyroidProblem,
              "heart_disease": heartDisease,
              "heart_murmur": heartMurmur,
              "hepatitis_liver_disease": hepatitisLiverDisease,
              "rheumatic_seizure": rheumaticSeizure,
              "respiratory_problems": respiratoryProblems,
              "hepatitis_jaundice": hepatitisJaundice,
              "tuberculosis": tuberculosis,
              "swollen_ankles": swollenAnkles,
              "kidney_disease": kidneyDisease,
              "other_diseases": others
            

           
          })
        });

       
    
        if (!response.ok) {
          throw new Error('Failed to register');
        }
        
        const data = await response.json();
        console.log('Server Response:', data);
    
        if(data.status_code === 200) {
          registerSuccessful = true;
        }
      } catch (error) {
        console.error('Registration error:', error);
        return false;
      }
    
      return registerSuccessful;
}
    