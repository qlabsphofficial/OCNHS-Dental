<script setup>
import HeaderComponent from '@/components/shared/HeaderComponent.vue';
import ClientNavbar from '@/components/client/main/ClientNavbar.vue';
import LoginView from './LoginView.vue';

// Dynamic Components

import { ref, shallowRef  } from 'vue';

const currentComponent = shallowRef(null) 

function handleUpdateModule(moduleName){
      switch(moduleName) {
            case 'appointment':
                  currentComponent.value = LoginView
                  break;

            case 'personalDetails':
                  break;

            case 'medicalHistory':
                  break;
      }
}
</script>


<template>
      <div class="w-full h-full top-0 left-0 absolute">
            <HeaderComponent />

            <div class="flex flex-row h-full w-full">
                  <ClientNavbar @update-module="handleUpdateModule" />
                  <component :is="currentComponent"></component>
            </div>
      </div>
</template>

<style scoped>

</style>