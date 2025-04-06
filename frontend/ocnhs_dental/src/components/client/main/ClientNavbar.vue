<script setup lang="ts">
import { defineEmits } from 'vue'; 

const emit = defineEmits()

function changeModule(moduleName) {
      console.log(moduleName)

      this.emit('update-module', {
            'moduleName': moduleName
      })
}
</script>

<template>
      <div class="h-full w-2/12 main-color text-white">
            <div class="flex flex-row justify-between items-center w-full h-1/12 p-5 bg-gray-500">
                  <img src="" alt="">
                  <h5>Username</h5>
                  <button>Settings</button>
            </div>

            <div class="flex flex-col items-start gap-10 p-5 mt-10">
                  <button type="button" @click="changeModule('appointment')">APPOINTMENT</button>
                  <button type="button" @click="changeModule('personalDetails')">PERSONAL DETAILS</button>
                  <button type="button" @click="changeModule('medicalHistory')">MEDICAL HISTORY</button>
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