<script setup lang="ts">
import { defineEmits, ref } from 'vue';
import { Book, ClipboardPlus, ScrollText, UserRound, Settings, LogOut  } from 'lucide-vue-next';
import { useRouter } from 'vue-router';

const emit = defineEmits()
const router = useRouter()
const showOptions = ref(false)
const loggedInUser = ref('')

loggedInUser.value = JSON.parse(sessionStorage.getItem('user'))

function changeModule(moduleName) {
      emit('update-module', {
            'moduleName': moduleName
      })
}
</script>

<template>
      <div class="h-5/12 lg:h-full lg:w-2/12 main-color text-white">
            <div class="flex flex-row justify-between items-center w-full h-2/12 lg:h-1/12 p-5 bg-gray-500">
                  <div class="flex flex-row gap-4 w-1/2">
                        <img src="" alt="">
                        <h5>{{ loggedInUser.firstname }} {{ loggedInUser.lastname }}</h5>
                  </div>

                  <div class="w-1/2 flex justify-end">
                        <div v-if="showOptions" class="flex flex-col gap-5 w-60 absolute bg-gray-300 top-34 lg:top-50 p-5 rounded-md">
                              <button class="flex flex-row justify-center gap-4" @click="() => { changeModule('settings'); showOptions = false; }"><Settings />Settings</button>
                              <button class="flex flex-row justify-center gap-4" @click="() => { router.push('/') } "><LogOut />Sign Out</button>
                        </div>
                        <button class="flex items-center gap-2">
                              <Settings class="w-5 h-5" @click="() => { showOptions = !showOptions }" />
                        </button>
                  </div>
            </div>

            <div class="flex flex-col items-start gap-10 p-5 lg:mt-10">
                  <button type="button" class="flex flex-row gap-4" @click="changeModule('appointment')"><ClipboardPlus /> APPOINTMENT</button>
                  <button type="button" class="flex flex-row gap-4" @click="changeModule('newAppointment')"><Book /> BOOK APPOINTMENT</button>
                  <button type="button" class="flex flex-row gap-4" @click="changeModule('personalDetails')"><UserRound /> PERSONAL DETAILS</button>
                  <button type="button" class="flex flex-row gap-4" @click="changeModule('medicalHistory')"><ScrollText /> MEDICAL HISTORY</button>
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