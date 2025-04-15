import current_address from "@/address";

export async function retrieveStudentRecords(fileType, year, curriculum, gradeLvl, section) {
    let studentRecords = []
    let requestBody = null

    // Make dynamic request to the endpoint
    if (fileType == 'CURRENT') {
        requestBody = {
            "is_archive": 0,
            "year": null,
            "curriculum": curriculum,
            "grade_level": gradeLvl,
            "section": section
        }
    }

    else {
        requestBody = {
            "is_archive": 1,
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