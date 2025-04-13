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
      message.value = await bookAppointment(category.value, date.value)

      setInterval(() => {
            message.value = ''
      }, 2000)
}
</script>

<template>
      <Transition>
            <div class="flex flex-col justify-evenly h-6/12 w-6/12 gap-5 p-10 border-2 rounded-md">
                  <div class="flex flex-row w-full justify-between">
                        <div class="flex flex-col">
                              <h1 class="text-3xl">Book an Appointment</h1>
                        </div>
      
                        <h2>{{ message }}</h2>
                  </div>
                  <hr>
      
                  <div class="flex flex-col gap-3 w-1/2 mt-2">
                        <h3 class="text-xl">Services Offered</h3>
                        <div class="w-1/2">
                              <select v-model="category" class="p-2 border-1">
                                    <option value="CLEANING">CLEANING</option>
                                    <option value="FLOURIDE">FLOURIDE</option>
                                    <option value="RESTORATION">RESTORATION</option>
                                    <option value="EXTRACTION">EXTRACTION</option>
                              </select>
                        </div>
      
                        <div class="mt-10">
                              <h3 class="text-xl">Schedule</h3>
                              <input type="datetime-local" v-model="date" class="mt-5 p-2 border-1" :min="selectedDate">
                        </div>
                  </div>
      
                  <div class="flex justify-center w-full">
                        <button class="border-2 p-2 text-center rounded-md w-full" @click="attemptBooking()">Book Now</button>
                  </div>
            </div>
      </Transition>
</template>

<style scoped>

</style>