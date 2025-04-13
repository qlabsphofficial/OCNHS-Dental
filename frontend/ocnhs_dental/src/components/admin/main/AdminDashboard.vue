<script setup>
import { retrieveAllAppointments, retrieveTodayAppointments } from '@/services/AppointmentService';
import { onMounted, ref, defineEmits } from 'vue';
import { User } from 'lucide-vue-next';

const emit = defineEmits()

const patientsToday = ref(0)
const totalPatients = ref(0)
const requests = ref(0)

const appointments = ref([])
const allAppointments = ref(0)
const monthlyAppointments = ref(0)
const appointmentsToday = ref([])

function formatDate(datetime) {
      if (!datetime) return '';
            const date = new Date(datetime);

      return date.toLocaleString('en-US', { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric', 
            hour: '2-digit', 
            minute: '2-digit', 
            hour12: true 
      });
}

function viewAllAppointments() {
      emit('view-all-appointments')
}

onMounted(async() => {
      let allAppointments = await retrieveAllAppointments() 
      let retrievedAppointmentsToday = await retrieveTodayAppointments()

      appointments.value = allAppointments
      requests.value = allAppointments.length
      appointmentsToday.value = retrievedAppointmentsToday
})
</script>

<template>
      <div class="flex flex-col h-11/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="flex flex-row items-between justify-between">
                  <div class="flex flex-row w-1/2 justify-evenly gap-4">
                        <div class="flex flex-col items-center justify-center w-1/3 border-2 rounded-md p-6">
                              <p>Patients Today</p>
                              <h2 class="text-5xl mt-2">{{ appointmentsToday.length }}</h2>
                        </div>

                        <div class="flex flex-col items-center justify-center w-1/3 border-2 rounded-md p-6">
                              <p>Total Patients</p>
                              <h2 class="text-5xl mt-2">{{ appointments.length }}</h2>
                        </div>

                        <div class="flex flex-col items-center justify-center w-1/3 border-2 rounded-md p-6">
                              <p>Requests</p>
                              <h2 class="text-5xl mt-2">{{ requests }}</h2>
                        </div>
                  </div>

                  <!-- Clock -->
                  <div>
                        
                  </div>
            </div>

            <div class="flex flex-row items-between justify-between mt-10 gap-5">
                  <div class="w-7/12 h-11/12">
                        <div class="flex flex-row items-center justify-between">
                              <h3 class="text-lg font-bold">Appointment Requests</h3>
                              <a @click="viewAllAppointments()" class="cursor-pointer">View All Appointments</a>
                        </div>
                        <div class="w-full flex flex-col gap-5 mt-5 overflow-y-scroll p-2 h-8/12">
                              <div v-for="appointment of appointments" :key="appointment" class="flex flex-row items-center justify-between bg-gray-100 rounded-md p-4">
                                    <div class="w-3/12 text-left">
                                          <h4>{{ appointment.student_info.firstname }} {{ appointment.student_info.last_name }}</h4>
                                    </div>

                                    <div class="w-2/12 text-left">
                                          <h4>{{ appointment.appointment_type }}</h4>
                                    </div>
                                    
                                    <div class="w-4/12 text-left">
                                          <h4>{{ formatDate(appointment.appointment_datetime) }}</h4>
                                    </div>
                                    
                                    <div class="w-3/12 ">
                                          <div v-if="appointment.status == 'PENDING'" class="flex items-center justify-center bg-yellow-300 rounded-md p-2">
                                                <h4>{{ appointment.status }}</h4>
                                          </div>

                                          <div v-else-if="appointment.status == 'APPROVED'" class="flex items-center justify-center bg-green-500 rounded-md p-2">
                                                <h4>{{ appointment.status }}</h4>
                                          </div>

                                          <div v-else-if="appointment.status == 'CANCELLED'" class="flex items-center justify-center bg-red-500 rounded-md p-2">
                                                <h4>{{ appointment.status }}</h4>
                                          </div>

                                          <div v-else-if="appointment.status == 'RESCHEDULED'" class="flex items-center justify-center bg-blue-500 rounded-md p-2">
                                                <h4>{{ appointment.status }}</h4>
                                          </div>
                                    </div>                                    
                              </div>
                        </div>
                  </div>

                  <div class="w-5/12 h-8/12 overflow-y-scroll">
                        <h3 class="text-lg font-bold">Appointments Today</h3>
                        <div class="flex flex-col gap-3 w-full overflow-y-scroll mt-8">
                              <div v-for="appointment of appointmentsToday" :key="appointment" class="flex flex-row items-center justify-between rounded-md bg-gray-100">
                                    <div class="flex flex-row items-center gap-5 p-5">
                                          <div class="flex items-center justify-center border-2 rounded-full">
                                                <User />
                                          </div>
                                          <div>
                                                <h4 class="text-xl font-bold">{{ appointment.student_info.firstname }} {{ appointment.student_info.last_name }}</h4>
                                                <p class="text-md">{{ appointment.appointment_type }}</p>
                                          </div>
                                    </div>

                                    <div>
                                          <h4>{{ formatDate(appointment.appointment_datetime) }}</h4>
                                    </div>
                                    <div></div>
                              </div>
                        </div>
                  </div>
            </div>
      </div>
</template>

<style scoped>

</style>