export async function retrieveMedicalHistory(id) {
      let medicalHistory = {}

      try {
            const response = await fetch(`${current_address}/get_student_medical_history?student_id=${id}`)
            const data = await response.json()

            medicalHistory = data
      }
      catch (error){

      }

      return medicalHistory
}

export async function retrieveAllMedicalHistory() {
      let medicalHistory = []

      // Insert medical history retrieval endpoint here

      return medicalHistory
}

export async function updateMedicalHistory(data) {
      // Insert medical history update endpoint here
}