<script setup>
import { ref } from 'vue';
import { register } from '@/services/RegisterService';
import { useRouter } from 'vue-router';

const firstName = ref('')
const middleName = ref('')
const lastName = ref('')
const suffix = ref('')

const birthDate = ref('')
const gender = ref('')
const age = ref('')
const placeOfBirth = ref('')

const contact = ref('')
const address = ref('')
const email = ref('')

const password = ref('')
const confirmPassword = ref('')

const router = useRouter()

async function attemptRegister() {
      const registerInfo = {
            firstName: firstName.value,
            middleName: middleName.value,
            lastName: lastName.value,
            suffix: suffix.value,

            birthDate: birthDate.value,
            gender: gender.value,
            age: age.value,
            placeOfBirth: placeOfBirth.value,

            contact: contact.value,
            address: address.value,
            email: email.value,

            password: password.value,
            confirmPassword: confirmPassword.value
      };

      let registerResult = await register(registerInfo)

      if (registerResult){
            router.push('/login')
      }
}
</script>

<template>
      <div class="flex items-center justify-center w-full h-full top-0 left-0 absolute bg-gray-500">
            <div class="flex flex-col gap-5 h-10/12 w-10/12 rounded-md bg-white p-20">
                  <div class="flex flex-row justify-between items-center w-full">
                        <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="240px" width="160px">
                        <h1 class="text-6xl">SIGN UP</h1>
                        <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="240px" width="160px">
                  </div>

                  <div class="flex flex-row justify-between w-full gap-5 mt-20">
                        <div class="w-3/12">
                              <h5>First Name</h5>
                              <input v-model="firstName" type="text" class="w-full bg-gray-300 p-4" placeholder="Enter your first name...">
                        </div>
                        <div class="w-3/12">
                              <h5>Middle Name</h5>
                              <input v-model="middleName" type="text" class="w-full bg-gray-300 p-4" placeholder="Enter your middle name...">
                        </div>
                        <div class="w-3/12">
                              <h5>Last Name</h5>
                              <input v-model="lastName" type="text" class="w-full bg-gray-300 p-4" placeholder="Enter your last name...">
                        </div>
                        <div class="w-3/12">
                              <h5>Suffix</h5>
                              <input v-model="suffix" type="text" class="w-full bg-gray-300 p-4">
                        </div>
                  </div>

                  <div class="flex flex-row justify-between w-full gap-5 mt-10">
                        <div class="w-3/12">
                              <h5>Date of Birth</h5>
                              <input v-model="birthDate" type="date">
                        </div>
                        <div class="w-3/12">
                              <h5>Gender</h5>
                              <select v-model="gender">
                                    <option value="Male">Male</option>
                                    <option value="Female">Female</option>
                              </select>
                        </div>
                        <div class="w-3/12">
                              <h5>Age</h5>
                              <input disabled="true" v-model="age" type="number">
                        </div>
                        <div class="w-3/12">
                              <h5>Birthplace</h5>
                              <input v-model="placeOfBirth" type="text" class="w-full bg-gray-300 p-4" placeholder="Enter your birthplace...">
                        </div>
                  </div>

                  <div class="flex flex-row justify-between w-full gap-5 mt-10">
                        <div class="w-4/12">
                              <h5>Contact Number</h5>
                              <input v-model="contact" class="w-full bg-gray-300 p-4" type="number" placeholder="Enter your contact number...">
                        </div>
                        <div class="w-4/12">
                              <h5>Address</h5>
                              <input v-model="address" class="w-full bg-gray-300 p-4" type="text" placeholder="Enter your address...">
                        </div>
                        <div class="w-4/12">
                              <h5>Email</h5>
                              <input v-model="email" type="email" class="w-full bg-gray-300 p-4" placeholder="Enter your birthplace...">
                        </div>
                  </div>

                  <div class="flex flex-row justify-between w-full gap-5 mt-10">
                        <div class="w-4/12">
                              <h5>Password</h5>
                              <input v-model="password" class="w-full bg-gray-300 p-4" type="password" placeholder="Enter your contact number...">
                        </div>
                        <div class="w-4/12">
                              <h5>Confirm Password</h5>
                              <input v-model="confirmPassword" class="w-full bg-gray-300 p-4" type="password" placeholder="Enter your address...">
                        </div>
                  </div>

                  <div class="flex flex-row items-center justify-center w-full gap-5 mt-5">
                        <button class="rounded-md border-1 w-2/12 p-2 main-color text-white" @click="attemptRegister()">Save</button>
                        <button class="rounded-md border-1 w-2/12 p-2" @click="() => { this.$router.push('/login') }">Cancel</button>
                  </div>
            </div>
      </div>
</template>

<style scoped>
button {
      transition: .4s;
}

.main-color {
      background-color: #3B6364;
}

.secondary-color {
      background-color: #E7E8FF;
}

.overlay-color {
      background-color: #80B1B1;
}

.overlay-color-2 {
      background-color: #9cc7be;
}
</style>