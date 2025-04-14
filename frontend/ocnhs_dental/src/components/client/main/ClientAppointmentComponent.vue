<script setup>
import { ref, onMounted } from 'vue';
import { retrieveAppointments, downloadParentsConsent } from '@/services/AppointmentService';
import { formatDate } from '@/services/FormattingService';

const appointments = ref([]);
const appointmentHistory = ref([]);

// receive data from the user here
// Use a store
onMounted(async() => {
      appointments.value = await retrieveAppointments()
})
</script>

<template>
      <div class="flex flex-col lg:flex-row w-full h-full lg:h-10/12 lg:w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="flex flex-col justify-items items-center lg:items-start gap-3 w-full lg:w-4/12">
                  <h2 class="text-2xl lg:text-lg font-bold">Appointments</h2>
                  <!-- <div v-if="appointments.length == 0">
                        <p>No appointments yet.</p>
                  </div> -->
                  <div class="flex flex-col gap-7 h-full w-full overflow-y-scroll p-5">
                        <div v-for="appointment of appointments" :key="appointment" class="flex flex-col border-2 rounded-md p-10 text-white bg-blue-400">
                              <h2 class="text-2xl">{{ appointment.appointment_type }}</h2>
                              <p>{{ formatDate(appointment.appointment_datetime) }}</p>
      
                              <div class="w-full flex justify-center items-center mt-5">
                                    <div class="rounded-md border-2 w-1/3 text-center bg-transparent">{{ appointment.status }}</div>
                              </div>
                        </div>
                  </div>
                  <button class="mt-5 border-2 p-2 cursor-pointer" @click="downloadParentsConsent()">Download Parent's Consent Form</button>
            </div>

            <div class="flex flex-col gap-3 items-center justify-center lg:items-start lg:justify-start w-full lg:w-1/2">
                  <h2 class="text-2xl lg:text-lg font-bold mt-10 lg:mt-0">Appointment History</h2>

                  <div v-for="appointmentRecord of appointments" :key="appointmentRecord" class="flex flex-col border-2 rounded-md p-10 w-full text-white bg-blue-400">
                        <h2 class="text-2xl">{{ appointmentRecord.appointment_type }}</h2>

                        <div class="flex flex-row items-center justify-between w-full">
                              <p>{{ formatDate(appointmentRecord.appointment_datetime) }}</p>
                              <div class="rounded-md border-2 w-1/3 text-center bg-transparent">{{ appointmentRecord.status }}</div>
                        </div>
                  </div>
            </div>
      </div>
</template>

<style scoped>

</style>