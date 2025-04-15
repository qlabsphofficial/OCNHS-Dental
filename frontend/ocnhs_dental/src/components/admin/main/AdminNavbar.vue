<script setup lang="ts">
import current_address from '@/address';
import { 
    Home, Calendar, Users, FileText, ClipboardList, FileSearch, BarChart, Settings, LogOut 
} from 'lucide-vue-next';
import { ref, defineEmits } from 'vue'; 
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';

const emit = defineEmits()
const showOptions = ref(false)
const router =  useRouter()
const userStore = useUserStore()

function changeModule(moduleName) {
      emit('update-module', {
            'moduleName': moduleName
      })
}

function attemptLogout() {
      emit('log-out')
}

async function downloadReport() {
  try {
    const response = await fetch(`${current_address}/generate_report`, {
      method: 'GET'
    });

    if (!response.ok) throw new Error('Download failed');

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'DENTAL ACCOMPLISHMENT REPORT.xlsx';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  } catch (error) {
    console.error('Error downloading the report:', error);
  }
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
                  <button type="button" @click="downloadReport()" class="flex items-center gap-5">
                        <BarChart class="w-5 h-5" /> REPORTS
                  </button>
            </div>

            <div class="flex flex-row justify-between items-center w-full h-1/12 p-5 bg-gray-500">
                  <div class="flex flex-row gap-4">
                        <img src="" alt="">
                        <h5>{{ userStore.user.firstname }} {{ userStore.user.lastname }}</h5>
                  </div>

                  <div>
                        <div v-if="showOptions" class="flex flex-col gap-5 w-60 absolute bg-gray-300 bottom-20 negative-margin p-5 rounded-md">
                              <button class="flex flex-row justify-center gap-4"><Settings />Settings</button>
                              <button class="flex flex-row justify-center gap-4" @click="attemptLogout()"><LogOut />Sign Out</button>
                        </div>
                        <button class="flex items-center gap-2">
                              <Settings class="w-5 h-5" @click="() => { showOptions = !showOptions }" />
                        </button>
                  </div>
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

.negative-margin {
      margin-top: -10%;
}
</style>