<script setup>
import HeaderComponent from '@/components/shared/HeaderComponent.vue';
import ClientNavbar from '@/components/client/main/ClientNavbar.vue';
import ClientSettingsComponent from '@/components/client/main/ClientSettingsComponent.vue';
import ClientAppointmentComponent from '@/components/client/main/ClientAppointmentComponent.vue';
import ClientNewAppointmentComponent from '@/components/client/main/ClientNewAppointmentComponent.vue';
import ClientPersonalDetailsComponent from '@/components/client/main/ClientPersonalDetailsComponent.vue';
import ClientMedicalHistory from '@/components/client/main/ClientMedicalHistory.vue';

// Dynamic Components

import { ref, shallowRef  } from 'vue';


const currentComponent = shallowRef(null) 

function handleUpdateModule(data){
      switch(data.moduleName) {
            case 'settings':
                  currentComponent.value = ClientSettingsComponent
                  break;

            case 'appointment':
                  currentComponent.value = ClientAppointmentComponent
                  break;

            case 'newAppointment':
                  currentComponent.value = ClientNewAppointmentComponent
                  break;

            case 'personalDetails':
                  currentComponent.value = ClientPersonalDetailsComponent
                  break;

            case 'medicalHistory':
                  currentComponent.value = ClientMedicalHistory
                  break;
      }
}
</script>


<template>
      <div class="w-full h-full top-0 left-0 absolute">
            <HeaderComponent />

            <div class="flex flex-row h-11/12 w-full">
                  <ClientNavbar @update-module="handleUpdateModule" />
                  <div class="flex items-center justify-center w-10/12 h-full">
                        <component :is="currentComponent"></component>
                  </div>
            </div>
      </div>
</template>

<style scoped>

</style>