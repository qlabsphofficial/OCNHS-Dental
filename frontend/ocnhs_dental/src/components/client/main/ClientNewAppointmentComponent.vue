<script setup>
import { ref } from 'vue';
import { bookAppointment } from '@/services/AppointmentService';

const category = ref('');
const date = ref('');
const message = ref('')

const now = new Date();
const pad = (n) => String(n).padStart(2, '0');
const today = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}T${pad(now.getHours())}:${pad(now.getMinutes())}`;
const selectedDate = ref(today)

// receive data from the user here
// Use a store
async function attemptBooking(){
      if (category.value == '' || date.value == ''){
            message.value = 'Please fill out the required fields.'

            setTimeout(() => {
                  message.value = ''
            }, 2000)

            return
      }

      message.value = await bookAppointment(category.value, date.value)

      setTimeout(() => {
            message.value = ''
            category.value = ''
            date.value = ''
      }, 2000)
}
</script>

<template>
      <div class="flex flex-col justify-evenly h-full w-full lg:h-6/12 lg:w-6/12 gap-2 lg:gap-5 p-10 lg:border-2 rounded-md lg:mt-0">
            <div class="flex flex-row w-full justify-between">
                  <div class="flex flex-col">
                        <h1 class="text-3xl font-bold">Book an Appointment</h1>
                  </div>

                  <h2>{{ message }}</h2>
            </div>

            <hr class="hidden lg:block">

            <div class="flex flex-col gap-3 w-full lg:w-1/2 mt-2">
                  <h3 class="text-xl">Services Offered</h3>
                  <div class="w-full lg:w-1/2">
                        <select v-model="category" class="p-2 border-1 w-full">
                              <option value="CLEANING">CLEANING</option>
                              <option value="FLOURIDE">FLOURIDE</option>
                              <option value="RESTORATION">RESTORATION</option>
                              <option value="EXTRACTION">EXTRACTION</option>
                        </select>
                  </div>

                  <div class="mt-10">
                        <h3 class="text-xl">Schedule</h3>
                        <input type="datetime-local" v-model="date" class="mt-5 p-2 border-1 w-full" :min="selectedDate">
                  </div>
            </div>

            <div class="flex justify-center w-full">
                  <button class="border-2 p-2 text-center rounded-md w-full" @click="attemptBooking()">Book Now</button>
            </div>
      </div>
</template>

<style scoped>

</style>