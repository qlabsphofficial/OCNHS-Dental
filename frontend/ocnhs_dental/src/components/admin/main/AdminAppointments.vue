<script setup>
import { ref, onMounted } from 'vue';
import { X, Check, CalendarSync  } from 'lucide-vue-next';
import { retrieveAllAppointments, approveAppointment, cancelAppointment, rescheduleAppointment } from '@/services/AppointmentService';

const page = ref('')
const appointments = ref([])
const chosenDates = ref({}); // Store chosen dates separately for each appointment

const now = new Date();
const pad = (n) => String(n).padStart(2, '0');

// Today's date
const yyyy = now.getFullYear();
const mm = pad(now.getMonth() + 1);
const dd = pad(now.getDate());

// Set min and max time on the same day
const minTime = `${yyyy}-${mm}-${dd}T08:00`;
const maxTime = `${yyyy}-${mm}-${dd}T17:00`;

const selectedDate = ref(minTime); // default value starts at 8:00AM


onMounted(async() => {
      appointments.value = await retrieveAllAppointments()
})

async function attemptApprove(id){
      approveAppointment(id)
      appointments.value = await retrieveAllAppointments()
}

async function attemptCancel(id){
      cancelAppointment(id)
      appointments.value = await retrieveAllAppointments()
}

async function attemptReschedule(id){
      rescheduleAppointment(id, chosenDates.value[id])
      chosenDates.value[id] = ''
      appointments.value = await retrieveAllAppointments()
}

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
</script>

<template>
      <div class="flex flex-col justify-between h-11/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="h-11/12 w-full overflow-y-scroll">
                  <h1 class="text-2xl font-bold mb-5">APPOINTMENTS</h1>

                  <table class="w-full h-auto">
                        <thead>
                              <tr class="border-2 sticky bg-white">
                                    <th class="text-lg">NAME</th>
                                    <th class="text-lg">SECTION</th>
                                    <th class="text-lg">DATE & TIME</th>
                                    <th class="text-lg">APPOINTMENT TYPE</th>
                                    <th class="text-lg">STATUS</th>
                                    <th class="text-lg">APPROVE</th>
                                    <th class="text-lg">CANCEL</th>
                                    <th class="text-lg">RESCHEDULE</th>
                              </tr>
                        </thead>
      
                        <!-- ITERATE THROUGH RECORDS HERE -->
                        <tr v-for="appointment, index in appointments" :key="appointment">
                              <td class="p-2">{{ index + 1 }}. {{ appointment.student_info.lastname }}, {{ appointment.student_info.firstname }} {{ appointment.student_info.middlename[0] }}</td>
                              <td class="text-center p-2">{{ appointment.student_info.section }}</td>
                              <td class="p-2">{{ formatDate(appointment.appointment_datetime) }}</td>
                              <td class="text-center p-2">{{ appointment.appointment_type }}</td>
                              <td class="text-center p-2">
                                    <div v-if="appointment.status == 'RESCHEDULED'" class="bg-blue-400 rounded-md p-2 text-white">{{ appointment.status }}</div>
                                    <div v-else-if="appointment.status == 'APPROVED'" class="bg-green-500 rounded-md p-2 text-white">{{ appointment.status }}</div>
                                    <div v-else-if="appointment.status == 'CANCELLED'" class="bg-red-500 rounded-md p-2 text-white">{{ appointment.status }}</div>
                              </td>
                              <td class="text-center p-2"><button @click="attemptApprove(appointment.appointment_id)" class="bg-transparent hover:bg-green-400 p-2 rounded-md transition duration-300 ease-in-out cursor-pointer"><Check /></button></td>
                              <td class="text-center p-2"><button @click="attemptCancel(appointment.appointment_id)" class="bg-transparent hover:bg-red-400 p-2 rounded-md transition duration-300 ease-in-out cursor-pointer"><X /></button></td>
                              <td class="text-center p-2">
                                    <div class="flex flex-row items-center justify-evenly gap-4">
                                          <input type="datetime-local" v-model="chosenDates[appointment.appointment_id]" :min="selectedDate" class="w-5/12 cursor-pointer">
                                          <button class="flex flex-row text-center gap-4 border-2 rounded-md p-2 hover:bg-gray-300 transition duration-300 ease-in-out cursor-pointer" @click="attemptReschedule(appointment.appointment_id)"><CalendarSync /> Submit</button>
                                    </div>
                              </td>
                        </tr>
                  </table>
            </div>
            
            <!-- <div class="flex flex-row justify-between w-full">
                  <p>Page: {{ page }}</p>
                  <div class="flex flex-row w-3/12 justify-evenly">
                        <button class="border-2 rounded-md p-1 w-5/12">Previous</button>
                        <button class="border-2 rounded-md p-1 w-5/12">Next</button>
                  </div>
            </div> -->
      </div>
</template>



<style scoped>

</style>