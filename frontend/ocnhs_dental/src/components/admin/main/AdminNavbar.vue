<script setup lang="ts">
import { 
    Home, Calendar, Users, FileText, ClipboardList, FileSearch, BarChart
} from 'lucide-vue-next';
import { defineEmits } from 'vue'; 

const emit = defineEmits()

function changeModule(moduleName) {
      this.emit('update-module', {
            'moduleName': moduleName
      })
}
</script>

<template>
      <div class="flex flex-col justify-between h-full w-2/12 main-color text-white">
            <div class="flex flex-col items-start gap-10 p-5 mt-10">
                  <button type="button" @click="changeModule('dashboard')" class="flex items-center gap-5">
                        <Home class="w-5 h-5" /> DASHBOARD
                  </button>
                  <button type="button" @click="changeModule('appointments')" class="flex items-center gap-5">
                        <ClipboardList class="w-5 h-5" /> APPOINTMENTS
                  </button>
                  <button type="button" @click="changeModule('calendar')" class="flex items-center gap-5">
                        <Calendar class="w-5 h-5" /> CALENDAR
                  </button>
                  <button type="button" @click="changeModule('studentRecord')" class="flex items-center gap-5">
                        <Users class="w-5 h-5" /> STUDENT RECORD
                  </button>
                  <button type="button" @click="changeModule('accounts')" class="flex items-center gap-5">
                        <FileText class="w-5 h-5" /> ACCOUNTS
                  </button>
                  <button type="button" @click="changeModule('dentalExam')" class="flex items-center gap-5">
                        <FileSearch class="w-5 h-5" /> DENTAL EXAM FORM
                  </button>
                  <button type="button" @click="changeModule('reports')" class="flex items-center gap-5">
                        <BarChart class="w-5 h-5" /> REPORTS
                  </button>
            </div>

            <div class="flex flex-row justify-between items-center w-full h-1/12 p-5 bg-gray-500">
                  <img src="" alt="">
                  <h5>Username</h5>
                  <button class="flex items-center gap-2">
                        <FileText class="w-5 h-5" /> Settings
                  </button>
            </div>
      </div>
</template>


<style scoped>
.main-color {
      background-color: #3B6364;
}

.secondary-color {
      background-color: #E7E8FF;
}

.overlay-color {
      background-color: #80B1B1;
}

.overlay-color-2 {
      background-color: #9cc7be;
}
</style>