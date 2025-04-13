<script setup>
import { ref, onMounted } from 'vue';
import { retrieveAppointments, downloadParentsConsent } from '@/services/AppointmentService';

const appointments = ref([]);
const appointmentHistory = ref([]);

// receive data from the user here
// Use a store
onMounted(async() => {
      appointments.value = await retrieveAppointments()
})
</script>

<template>
      <div class="flex flex-row h-10/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="flex flex-col gap-3 w-4/12">
                  <h2 class="text-lg">Appointments</h2>
                  <!-- <div v-if="appointments.length == 0">
                        <p>No appointments yet.</p>
                  </div> -->
                  <div class="flex flex-col gap-10 h-full w-full overflow-y-scroll p-5">
                        <div v-for="appointment of appointments" :key="appointment" class="flex flex-col border-2 rounded-md p-10">
                              <h2 class="text-2xl">{{ appointment.appointment_type }}</h2>
                              <p>{{ appointment.appointment_datetime }}</p>
      
                              <div class="w-full flex justify-center items-center mt-5">
                                    <div class="bg-white rounded-md border-2 w-1/3 text-center">{{ appointment.status }}</div>
                              </div>
                        </div>
                  </div>
                  <button class="mt-5 border-2 p-2" @click="downloadParentsConsent()">Download Parent's Consent Form</button>
            </div>
            <div class="flex flex-col gap-3 w-1/2">
                  <h2 class="text-lg">Appointment History</h2>
                  <div v-for="appointmentRecord of appointmentHistory" :key="appointmentRecord">

                  </div>
            </div>
      </div>
</template>

<style scoped>

</style>