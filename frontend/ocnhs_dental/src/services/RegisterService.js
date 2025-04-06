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
      confirmPassword
    }) {
      let registerSuccessful = false;
      
      try {
        const response = await fetch('http://127.0.0.1:8000/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            'firstname': firstName,
            'middlename': middleName,
            'lastname': lastName,
            'suffix': suffix,
            'dateofbirth': birthDate,
            'gender': gender,
            'age': age,
            'birthplace': placeOfBirth,  
            'contact_no': contact,
            'address': address,
            'email_address': email,
            password: password,
            confirm_password: confirmPassword
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
    