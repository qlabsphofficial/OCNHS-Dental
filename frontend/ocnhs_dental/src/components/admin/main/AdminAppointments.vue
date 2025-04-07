<script setup>
import { ref, onMounted } from 'vue';
import { X, Check, CalendarSync  } from 'lucide-vue-next';
import { retrieveAllAppointments } from '@/services/AppointmentService';

const page = ref('')
const appointments = ref([])

onMounted(async() => {
      appointments.value = await retrieveAllAppointments()
})
</script>

<template>
      <div class="flex flex-col justify-between h-11/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <table>
                  <tr class="border-2">
                        <th class="text-lg">NAME</th>
                        <th class="text-lg">SECTION</th>
                        <th class="text-lg">DATE & TIME</th>
                        <th class="text-lg">APPOINTMENT TYPE</th>
                        <th class="text-lg">STATUS</th>
                        <th class="text-lg">APPROVE</th>
                        <th class="text-lg">CANCEL</th>
                        <th class="text-lg">RESCHEDULE</th>
                  </tr>

                  <!-- ITERATE THROUGH RECORDS HERE -->
                  <tr v-for="appointment, index of appointments" :key="appointment">
                        <td class="p-2">{{ index + 1 }}. {{ appointment.student_info.lastname }}, {{ appointment.student_info.firstname }} {{ appointment.student_info.middlename[0] }}</td>
                        <td class="text-center p-2">{{ appointment.student_info.section }}</td>
                        <td class="text-center p-2">{{ appointment.appointment_datetime }}</td>
                        <td class="text-center p-2">{{ appointment.appointment_type }}</td>
                        <td class="text-center p-2">{{ appointment.status }}</td>
                        <td class="text-center p-2"><button><Check /></button></td>
                        <td class="text-center p-2"><button><X /></button></td>
                        <td class="text-center p-2"><button><CalendarSync /></button></td>
                  </tr>
            </table>
            
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