import current_address from "@/address";

export async function updateDentalExam(student_id, layer_no, cell_no, value) {
    try {
    const response = await fetch(`${current_address}/create_condition_treatment_need`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'student_id': student_id,
            "layer_no": layer_no,
            "cell_no": cell_no,
            "value": value
        })
    });
    
    if (!response.ok) {
        throw new Error('Failed to update dental exaxm.');
    }
    
    const data = await response.json();
    console.log('Server Response:', data);
    
    if(data.message == "Data saved successfully!") {
        return
    }
    } catch (error) {
        console.error('Registration error:', error);
        return false;
    }
}

export async function updateDentalExamMultiple(student_id, layer_no, cell_no, value) {
    try {
    const response = await fetch(`${current_address}/create_condition_treatment_needs_array`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'student_id': student_id,
            "layer_no": layer_no,
            "cell_no": cell_no,
            "values": value
        })
    });
    
    if (!response.ok) {
        throw new Error('Failed to update dental exaxm.');
    }
    
    const data = await response.json();
    console.log('Server Response:', data);
    
    if(data.message == "Data saved successfully!") {
        return
    }
    } catch (error) {
        console.error('Registration error:', error);
        return false;
    }
}

export async function getDentalExam(student_id) {
    let layerData = []

    try {
        const response = await fetch(`${current_address}/get_condition_treatment_needs/${student_id}`);
        
        if (!response.ok) {
            throw new Error('Failed to get dental records.');
        }
        
        const data = await response.json();
        layerData = data
        
        console.log(layerData)
        
    } catch (error) {
        console.error('Retrieva; error:', error);
        return false;
    }

    return layerData
}