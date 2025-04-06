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

      console.log(firstName)
      console.log(lastName)
      console.log(email)
      console.log(password)
      console.log(confirmPassword)
    
      // INSERT REGISTER FUNCTIONALITY HERE
      if (firstName && lastName && email && password && password === confirmPassword) {
        registerSuccessful = true;
      }
    
      return registerSuccessful;
}
    