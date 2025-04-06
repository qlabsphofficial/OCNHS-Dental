<script setup lang="ts">
import { defineEmits, ref } from 'vue';
import { ClipboardPlus, ScrollText, UserRound, Settings, LogOut  } from 'lucide-vue-next';
import { useRouter } from 'vue-router';

const emit = defineEmits()
const router = useRouter()
const showOptions = ref(false)

function changeModule(moduleName) {
      emit('update-module', {
            'moduleName': moduleName
      })
}
</script>

<template>
      <div class="h-full w-2/12 main-color text-white">
            <div class="flex flex-row justify-between items-center w-full h-1/12 p-5 bg-gray-500">
                  <div class="flex flex-row gap-4">
                        <img src="" alt="">
                        <h5>Username</h5>
                  </div>

                  <div>
                        <div v-if="showOptions" class="flex flex-col gap-5 w-60 absolute bg-gray-300 top-50 p-5 rounded-md">
                              <button class="flex flex-row justify-center gap-4"><Settings />Settings</button>
                              <button class="flex flex-row justify-center gap-4" @click="() => { router.push('/') } "><LogOut />Sign Out</button>
                        </div>
                        <button class="flex items-center gap-2">
                              <Settings class="w-5 h-5" @click="() => { showOptions = !showOptions }" />
                        </button>
                  </div>
            </div>

            <div class="flex flex-col items-start gap-10 p-5 mt-10">
                  <button type="button" class="flex flex-row gap-4" @click="changeModule('appointment')"><ClipboardPlus /> APPOINTMENT</button>
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