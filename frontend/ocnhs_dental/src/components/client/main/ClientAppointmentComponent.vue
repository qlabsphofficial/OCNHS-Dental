<script setup>
import { ref } from 'vue';

const appointments = ref([]);
const appointmentHistory = ref([]);

// receive data from the user here
// Use a store
</script>

<template>
      <div class="flex flex-row h-10/12 w-11/12 gap-5 p-10 border-2 rounded-md">
            <div class="flex flex-col gap-3 w-1/2">
                  <h2 class="text-lg">Appointments</h2>
                  <div v-for="appointment of appointments" :key="appointment">

                  </div>
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