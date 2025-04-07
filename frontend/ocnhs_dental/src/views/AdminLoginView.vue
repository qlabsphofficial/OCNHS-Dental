<script setup>
import { login } from '@/services/LoginService'
import { ref } from 'vue'
import { useRouter } from 'vue-router' // Import Vue Router

const username = ref('')
const password = ref('')
const errorMessage = ref()
const router = useRouter() // Initialize router

async function attemptLogin() {
  try {
    const attempt = await login(username.value, password.value) // No "this", use .value

    if (attempt) {
      router.push('/admin') // Navigate to home if login is successful
    } else {
      errorMessage.value = 'Invalid credentials'
      setTimeout(() => {
      errorMessage.value = ''
      }, 2000)
    }
  } catch (error) {
    errorMessage.value = 'Login failed. Please try again later.'
    console.error(error)
  }
}
</script>

<template>
  <div class="flex flex-row w-full h-full top-0 left-0 absolute bg-black">
      <!-- Login Banner -->
      <div id="banner" class="h-full w-1/2"></div>

      <!-- Login -->
      <div class="flex flex-col items-center justify-center h-full w-1/2 bg-white p-20">
        <div class="flex flex-row justify-between w-full">
          <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="240px" width="160px">
          <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="240px" width="160px">
        </div>

        <h1 class="text-4xl mt-5">ADMIN LOGIN</h1>

        <div class="flex flex-col items-center w-7/12">       
          <!-- For checking login status -->
          <div v-if="errorMessage" id="error" class="flex items-center justify-center mt-10 mb-5 w-full p-2 rounded-md">
            <p>{{ errorMessage }}</p>
          </div>

          <div class="w-full">
            <h5 class="mb-5">Email Address</h5>
            <input v-model="username" type="email" placeholder="Enter your email address..." class="w-full rounded-md p-3 bg-gray-300">
          </div>

          <div class="w-full">
            <h5 class="mb-5 mt-10">Password</h5>
            <input v-model="password" type="password" placeholder="Enter your password..." class="w-full rounded-md p-3 bg-gray-300">
          </div>
          
          <button @click="attemptLogin()" id="submit" class="w-full rounded-md mt-10 mb-20 p-3">Login</button>

          <p>DON'T HAVE AN ACCOUNT? <a @click="() => { router.push('/adminSignUp') }">CLICK HERE</a></p>
          <a href="" class="mt-5">FORGOT PASSWORD</a>
        </div>
      </div>
  </div>
</template>

<style scoped>
#submit {
  color: white;
  background-color: #68c263;
  transition: .4s;
}

#error {
  color: white;
  background-color: #dc9c3a;
}

#banner {
  background: url('@/assets/Clinic Assets/Dental Clinic images/image/login.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>