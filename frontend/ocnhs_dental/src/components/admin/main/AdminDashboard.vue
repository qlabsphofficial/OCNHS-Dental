<script setup>
import { retrieveAllAppointments } from '@/services/AppointmentService';
import { onMounted, ref } from 'vue';

const patientsToday = ref(0)
const totalPatients = ref(0)
const requests = ref(0)

const appointments = ref([])
const appointmentsToday = ref([])

onMounted(async() => {
      let allAppointments = await retrieveAllAppointments() 

      appointments.value = allAppointments
      requests.value = allAppointments.length
})
</script>

<template>
      <div class="flex flex-col h-11/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="flex flex-row items-between justify-between">
                  <div class="flex flex-row w-1/2 justify-evenly gap-4">
                        <div class="flex flex-col items-center justify-center w-1/3 border-2 rounded-md p-6">
                              <div>
                                    <p>Patients Today</p>
                              </div>

                              <h2 class="text-5xl mt-2">{{ patientsToday }}</h2>
                        </div>

                        <div class="flex flex-col items-center justify-center w-1/3 border-2 rounded-md p-6">
                              <div>
                                    <p>Total Patients</p>
                              </div>

                              <h2 class="text-5xl mt-2">{{ totalPatients }}</h2>
                        </div>

                        <div class="flex flex-col items-center justify-center w-1/3 border-2 rounded-md p-6">
                              <div>
                                    <p>Requests</p>
                              </div>

                              <h2 class="text-5xl mt-2">{{ requests }}</h2>
                        </div>
                  </div>

                  <!-- Clock -->
                  <div>
                        
                  </div>
            </div>

            <div class="flex flex-row items-between justify-between mt-10">
                  <div class="w-1/2">
                        <h3 class="text-lg">Appointment Requests</h3>
                        <div class="w-full flex flex-col gap-3 mt-5 overflow-y-scroll p-2">
                              <div v-for="appointment of appointments" :key="appointment" class="flex flex-row items-between justify-between bg-gray-300 rounded-md p-4">
                                    <h4>{{ appointment.student_info.firstname }}  {{ appointment.student_info.last_name }}</h4>
                                    <h4>{{ appointment.appointment_type }}</h4>
                                    <h4>{{ appointment.appointment_datetime }}</h4>
                                    <h4>{{ appointment.status }}</h4>
                              </div>
                        </div>
                  </div>

                  <div class="w-1/2">
                        <h3 class="text-lg">Appointments Today</h3>
                        <div>
                              
                        </div>
                  </div>
            </div>
      </div>
</template>

<style scoped>

</style>