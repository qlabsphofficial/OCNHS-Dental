import { useUserStore } from "@/stores/user";
import current_address from "@/address";

export async function retrieveAppointments() {
      let appointments = [];
      let userStore = useUserStore()

      try {
            const response = await fetch(`${current_address}/get_student_appointments?student_id=${userStore.user.id}`)
            const data = await response.json()

            appointments = data.appointments
      }
      catch (error){

      }

      return appointments
}

export async function retrieveAllAppointments() {
      let appointments = [];

      try {
            const response = await fetch(`${current_address}/get_all_appointments`)
            const data = await response.json()

            appointments = data.appointments
      }
      catch (error){

      }

      return appointments
}



export async function retrieveAppointmentHistory() {
      let appointmentHistory = [];

      // Insert appointment retrieval endpoint here

      return appointmentHistory
}

export async function bookAppointment(category, date) {
      let userStore = useUserStore()
      let message = 'Booking Failed';

      // INSERT LOGIN FUNCTIONALITY HERE
      try {
      const response = await fetch(`${current_address}/create_appointment`, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                  'student_id': userStore.user.id,
                  "appointment_type": category,
                  "appointment_datetime": date,
                  "status": "PENDING"
            })
      });
      
      if (!response.ok) {
            throw new Error('Failed to book appointment');
      }
      
      const data = await response.json();
      console.log('Server Response:', data);
      
      if(data.message == "Appointment created successfully") {
            // Set data in sessionStorage
            message = 'Booking Successful';
      }
      } catch (error) {
            console.error('Registration error:', error);
      return false;
      }

      return message
}

export async function approveAppointment(id) {
      try {
      const response = await fetch(`${current_address}/approve_appointment`, {
            method: 'PUT',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                  'appointment_id': id,
            })
      });
      
      if (!response.ok) {
            throw new Error('Failed to approve appointment');
      }
      
      const data = await response.json();
      console.log('Server Response:', data);
      
      if(data.message == "Appointment approved successfully") {

      }
      } catch (error) {
            console.error('Approval error:', error);
      return false;
      }
}

export async function cancelAppointment(id) {
      try {
      const response = await fetch(`${current_address}/cancel_appointment`, {
            method: 'PUT',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                  'appointment_id': id,
            })
      });
      
      if (!response.ok) {
            throw new Error('Failed to cancel appointment');
      }
      
      const data = await response.json();
      console.log('Server Response:', data);
      
      if(data.message == "Appointment cancelled successfully") {

      }
      } catch (error) {
            console.error('Cancel error:', error);
      return false;
      }
}

export async function rescheduleAppointment(id, date) {
      try {
      const response = await fetch(`${current_address}/reschedule_appointment`, {
            method: 'PUT',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                  'appointment_id': id,
                  'date': date
            })
      });
      
      if (!response.ok) {
            throw new Error('Failed to reschedule appointment');
      }
      
      const data = await response.json();
      console.log('Server Response:', data);
      
      if(data.message == "Appointment rescheduled successfully") {

      }
      } catch (error) {
            console.error('Reschedule error:', error);
      return false;
      }
}