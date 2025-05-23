import current_address from "@/address";
import { useUserStore } from "@/stores/user";

export async function login(email, password) {
      let userStore = useUserStore()
      let loginSuccessful = false;

      // INSERT LOGIN FUNCTIONALITY HERE
      try {
            const response = await fetch(`${current_address}/login`, {
                  method: 'POST',
                  headers: {
                  'Content-Type': 'application/json'
                  },
                  body: JSON.stringify({
                  'email_address': email,
                  'password': password,
                  })
            });
            
            if (!response.ok) {
                  throw new Error('Failed to register');
            }
            
            const data = await response.json();
            console.log('Server Response:', data);
            
            if(data.message === "Login successful") {
                  // Set data in sessionStorage
                  sessionStorage.setItem('user', JSON.stringify(data.student_data));
                  sessionStorage.setItem('medical_history', JSON.stringify(data.medical_history));

                  userStore.user = JSON.parse(sessionStorage.getItem('user'))
                  userStore.medicalHistory = data.medical_history_status
                  
                  loginSuccessful = true;
            }
            
      } catch (error) {
            console.error('Registration error:', error);
            return false;
      }

      return loginSuccessful
}

export async function resetPassword(encryptedEmail, newPassword, confirmNewPassword) {
      console.log(encryptedEmail);
      let resetPasswordSuccessful = false;
    
      try {
        const response = await fetch(`${current_address}/reset_password/${encryptedEmail}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            new_password: newPassword,
            confirm_new_password: confirmNewPassword
          })
        });
    
        if (!response.ok) {
          throw new Error('Password change failed');
        }
    
        const data = await response.json();
        console.log('Server Response:', data);
    
        if (data.status_code == 200) {
          resetPasswordSuccessful = true;
        }
    
      } catch (error) {
        console.error('Password change error:', error);
        return false;
      }
    
      return resetPasswordSuccessful;
    }
    