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

            console.log(medicalHistory);
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

export async function updateMedicalHistory(data) {

}