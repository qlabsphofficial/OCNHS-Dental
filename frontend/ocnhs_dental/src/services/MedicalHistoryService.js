import current_address from "@/address";

export async function retrieveMedicalHistory(id) {
      let medicalHistory = {}

      try {
            const response = await fetch(`${current_address}/get_student_medical_history`, {
                  method: 'POST',
                  headers: {
                  'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                        'student_id': id
                  })
            })

            const data = await response.json()

            medicalHistory.student = data.student
            medicalHistory.medicalHistory = data.medical_history
      }
      catch (error){
            console.log(error);
      }

      return medicalHistory
}

export async function retrieveAllMedicalHistory() {
      let medicalHistory = []

      return medicalHistory
}

export async function updateMedicalHistory({
      studentID,
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
      dentistVisits
}) {

      let updateSuccessful = false;
      
      try {
        const response = await fetch(`${current_address}/update_student_medical_history`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              "student_id": studentID,
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
          })
        });

       
    
        if (!response.ok) {
          throw new Error('Failed to update');
        }
        
        const data = await response.json();
        console.log('Server Response:', data);
    
        if(data.status_code === 200) {
            updateSuccessful = true;
        }
      } catch (error) {
        console.error('Update error:', error);
        return false;
      }
    
      return updateSuccessful;

}