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