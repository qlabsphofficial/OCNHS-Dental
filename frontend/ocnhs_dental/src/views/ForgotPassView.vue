<script setup>
import { ref } from 'vue';
import { forgotPassword } from '@/services/RegisterService';

const email = ref('')
const emailSuccess = ref(false)

async function attemptEmail(){
    emailSuccess.value = await forgotPassword(email.value)
    email.value = ''
}
</script>

<template>
    <div class="flex items-center justify-center absolute top-0 left-0 w-full h-full bg-gray-200">
        <div class="flex flex-col justify-between items-center w-3/6 h-5/6 bg-white rounded-md shadow-md p-35">
            <div class="flex flex-row justify-between w-full">
                <img src="" alt="">
                <h3 class="text-2xl font-bold">FORGOT PASSWORD</h3>
                <img src="" alt="">
            </div>

            <input type="email" placeholder="Enter your email address" class="w-full border p-3 rounded-md" v-model="email">

            <div v-if="!emailSuccess">
                <p>
                    Enter the email address you used when you registered your account and we'll send you instructions to reset your password.
                </p>

                <p class="mt-2">
                    For security reasons, we DO NOT store your password. So rest assured that we will never send your password via email.
                </p>
            </div>

            <div v-else>
                <p class="text-green-500">A confirmation link has been sent to this email. Please verify that you have received the email.</p>
            </div>

            <button v-if="!emailSuccess" class="w-3/4 h-10 rounded-md text-white bg-blue-500 text-center" @click="attemptEmail()">RESET PASSWORD</button>
        </div>
    </div>
</template>

<style scoped>
</style>
