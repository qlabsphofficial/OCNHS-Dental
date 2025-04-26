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
      router.push('/client')
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
      <div id="banner" class="h-full w-1/2 hidden lg:block"></div>

      <!-- Login -->
      <div class="flex flex-col items-center justify-center h-full w-full lg:w-1/2 bg-white lg:p-20">
        <div class="flex flex-row justify-evenly items-center w-full">
          <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="240px" width="160px" class="hidden lg:block">
          <h1 class="text-4xl mt-5">LOGIN</h1>
          <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="240px" width="160px" class="hidden lg:block">
        </div>

        

        <div class="flex flex-col items-center w-10/12 lg:w-7/12 mt-10">       
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
          
          <button @click="attemptLogin()" class="w-full rounded-md mt-10 mb-20 p-3 cursor-pointer bg-green-400 hover:bg-transparent border border-transparent hover:border-green-500 transition duration-300 ease-in-out">Login</button>

          <p>DON'T HAVE AN ACCOUNT? <a @click="() => { router.push('/signUp') }" class="cursor-pointer">CLICK HERE</a></p>
          <a @click="() => { router.push('/forgotPassword') }" class="mt-5 cursor-pointer">FORGOT PASSWORD</a>
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