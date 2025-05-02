import current_address from "@/address";

export async function retrieveStudentRecords(fileType, year, curriculum, gradeLvl, section) {
    let studentRecords = []
    let requestBody = null

    // Make dynamic request to the endpoint
    if (fileType == 'CURRENT') {
        requestBody = {
            "is_archive": false,
            "year": null,
            "curriculum": curriculum,
            "grade_level": gradeLvl,
            "section": section
        }
    }

    else {
        requestBody = {
            "is_archive": true,
            "year": year,
            "curriculum": curriculum,
            "grade_level": null,
            "section": null
        }
    }

    try {
        const response = await fetch(`${current_address}/get_students`, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });
        
        if (!response.ok) {
            throw new Error('Failed to get student records.');
        }
        
        const data = await response.json();
        studentRecords = data.students
        console.log('Server Response:', data);

        
        } catch (error) {
            console.error('Registration error:', error);

        return false;
    }

    return studentRecords
}

export async function updateArchiveStatus({
    studentID,
    isArchive,
}) {

    let updateSuccessful = false;
    
    try {
      const response = await fetch(`${current_address}/update_archive_status`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "student_id": studentID,
            "is_archive": isArchive,
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

export async function deleteStudentRecord(id) {

    let deleteSuccessful = false;
    
    try {
      const response = await fetch(`${current_address}/delete_student_record`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "student_id": id
        })
      });

      if (!response.ok) {
        throw new Error('Failed to delete');
      }
      
      const data = await response.json();
      console.log('Server Response:', data);
  
      if(data.status_code === 200) {
        deleteSuccessful = true;
      }
    } catch (error) {
      console.error('Delete error:', error);
      return false;
    }
  
    return deleteSuccessful;
}

export async function submitTemporaryTeethData({
  temporaryTeethData
}) {
  let submissionSuccessful = false;

  try {
    // Send all records as a bulk POST request
    const response = await fetch(`${current_address}/create_temp_teeth_bulk`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(temporaryTeethData) // Send the whole list of records
    });

    if (!response.ok) {
      throw new Error('Failed to submit data');
    }

    const data = await response.json();
    console.log('Bulk submission successful:', data);

    if (data.status_code !== 200) {
      throw new Error('Server returned error');
    }

    submissionSuccessful = true;
  } catch (error) {
    console.error('Submission error:', error);
    return false;
  }

  return submissionSuccessful;
}

export const fetchTemporaryTeeth = async (studentID) => {
  try {
    const response = await fetch(`${current_address}/get_temporary_teeth/${studentID}`);

    if (response.status === 404) {
      // No data found is not an error in our case — return an empty array
      return [];
    }

    if (!response.ok) {
      throw new Error("Failed to fetch Temporary Teeth records");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching Temporary Teeth:", error);
    throw error;
  }
};

export async function submitPermanentTeethData({
  PermanentTeethData
}) {
  let submissionSuccessful = false;

  try {
    // Send all records as a bulk POST request
    const response = await fetch(`${current_address}/create_perma_teeth_bulk`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(PermanentTeethData) // Send the whole list of records
    });

    if (!response.ok) {
      throw new Error('Failed to submit data');
    }

    const data = await response.json();
    console.log('Bulk submission successful:', data);

    if (data.status_code !== 200) {
      throw new Error('Server returned error');
    }

    submissionSuccessful = true;
  } catch (error) {
    console.error('Submission error:', error);
    return false;
  }

  return submissionSuccessful;
}

export const fetchPermanentTeeth = async (studentID) => {
  try {
    const response = await fetch(`${current_address}/get_permarnent_teeth/${studentID}`);

    if (response.status === 404) {
      // No data found is not an error in our case — return an empty array
      return [];
    }
    
    if (!response.ok) {
      throw new Error("Failed to fetch Temporary Teeth records");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching Temporary Teeth:", error);
    throw error;
  }
};

export async function submitOralHealthConditionData({
  OralHealthConditionData
}) {
  let submissionSuccessful = false;

  try {
    // Send all records as a bulk POST request
    const response = await fetch(`${current_address}/create_oral_health_condition_bulk`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(OralHealthConditionData) // Send the whole list of records
    });

    if (!response.ok) {
      throw new Error('Failed to submit data');
    }

    const data = await response.json();
    console.log('Bulk submission successful:', data);

    if (data.status_code !== 200) {
      throw new Error('Server returned error');
    }

    submissionSuccessful = true;
  } catch (error) {
    console.error('Submission error:', error);
    return false;
  }

  return submissionSuccessful;
}

export const fetchOralHealthCondition = async (studentID) => {
  try {
    const response = await fetch(`${current_address}/get_oral_health_condition_teeth/${studentID}`);

    if (response.status === 404) {
      // No data found is not an error in our case — return an empty array
      return [];
    }
    
    if (!response.ok) {
      throw new Error("Failed to fetch Temporary Teeth records");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching Temporary Teeth:", error);
    throw error;
  }
};

export async function submitDentalProcedureData({
  DentalProcedureData
}) {
  let submissionSuccessful = false;

  try {
    // Send all records as a bulk POST request
    const response = await fetch(`${current_address}/create_dental_procedure_bulk`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(DentalProcedureData) // Send the whole list of records
    });

    if (!response.ok) {
      throw new Error('Failed to submit data');
    }

    const data = await response.json();
    console.log('Bulk submission successful:', data);

    if (data.status_code !== 200) {
      throw new Error('Server returned error');
    }

    submissionSuccessful = true;
  } catch (error) {
    console.error('Submission error:', error);
    return false;
  }

  return submissionSuccessful;
}

export const fetchDentalProcedure = async (studentID) => {
  try {
    const response = await fetch(`${current_address}/get_dental_procedure_teeth/${studentID}`);

    if (response.status === 404) {
      // No data found is not an error in our case — return an empty array
      return [];
    }
    
    if (!response.ok) {
      throw new Error("Failed to fetch Temporary Teeth records");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching Temporary Teeth:", error);
    throw error;
  }
};