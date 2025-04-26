<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router'
import { resetPassword } from '@/services/LoginService'

const route = useRoute()
const router = useRouter()
const encryptedEmail = route.params.encryptedEmail
const decryptedEmail = ref('')

const showResetForms = ref(false)

const password = ref('')
const confirmPassword = ref('')

function caesarDecrypt(text, shift) {
  let result = ''
  for (let i = 0; i < text.length; i++) {
    const char = text[i]
    if (char.match(/[a-z]/i)) {
      const code = text.charCodeAt(i)
      let base = code >= 65 && code <= 90 ? 65 : 97
      result += String.fromCharCode(((code - base - shift + 26) % 26) + base)
    } else {
      result += char
    }
  }
  return result
}

async function resetPasswordAction() {
  try {
    const resetPasswordSuccess = await resetPassword(encryptedEmail, password.value, confirmPassword.value);

    if (resetPasswordSuccess) {
      router.push('/login');
    } 

  } catch (error) {
    console.error(error);
  }
}

onMounted(() => {
  decryptedEmail.value = caesarDecrypt(encryptedEmail, 3)
})

</script>

<template>
    <div class="flex items-center justify-center absolute top-0 left-0 w-full h-full bg-gray-200">
        <div class="flex flex-col justify-evenly items-center w-3/6 h-5/6 bg-white rounded-md shadow-md p-16 pl-35 pr-35">
            <div v-if="!showResetForms">
                <div class="flex flex-row justify-between w-full">
                    <img src="" alt="">
                    <h3 class="text-4xl font-bold">OCNHS DENTAL CLINIC</h3>
                    <img src="" alt="">
                </div>

                <div>
                    <p>Hi there,</p>

                    <p class="mt-2">
                        A password reset request has been submitted for the OCNHS Dental Clinic account linked to <span class="underline">{{ decryptedEmail }}</span>.
                        No modifications have been applied to the account at this time.
                    </p>

                    <p class="mt-2">To reset your password, please click on the following link:</p>

                    <div class="flex justify-center items-center w-full mt-10 mb-10">
                        <button class="w-3/4 h-10 rounded-md text-white bg-blue-500 text-center" @click="() => { showResetForms = true }">RESET PASSWORD</button>
                    </div>
                    
                    <p>If you did not request a new password, please let us know immediately by replying to this email.</p>

                    <p class="mt-10">OCNHS Dental Clinic</p>
                    <p>Admin</p>
                </div>
            </div>

            <div v-else class="flex flex-col items-center justify-center">
                <h3 class="text-4xl font-bold">RESET ACCOUNT PASSWORD</h3>
                <p class="mt-26">ENTER THE NEW PASSWORD FOR {{ decryptedEmail }}.</p>

                <div class="flex flex-col justify-center items-center gap-2 w-full mt-5">
                    <input type="password" class="w-11/12 border p-2 border" v-model="password" placeholder="Enter your password...">
                    <input type="password" class="w-11/12 border p-2 border" v-model="confirmPassword" placeholder="Confirm password...">
                </div>

                <button class="rounded-md text-center text-white bg-blue-500 p-2 w-3/4 mt-20" @click="resetPasswordAction()">RESET PASSWORD</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>
