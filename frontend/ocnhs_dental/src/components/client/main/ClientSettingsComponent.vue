<script setup>
import { shallowRef } from 'vue'
import { UserPen } from 'lucide-vue-next';
import { ShieldCheck } from 'lucide-vue-next';

import ClientEditProfileComponent from '@/components/client/main/ClientEditProfileComponent.vue';
import ClientSecurityComponent from '@/components/client/main/ClientSecurityComponent.vue';

const currentComponent = shallowRef(ClientEditProfileComponent)

function changeModule (component) {
    switch(component) {
        case 'edit':
            currentComponent.value = ClientEditProfileComponent
            break;

        case 'security':
            currentComponent.value = ClientSecurityComponent
            break;
    }
}
</script>

<template>
    <div class="flex flex-col lg:flex-row gap-4 h-full w-full lg:w-11/12 lg:h-10/12 p-4 lg:border-2 lg:rounded-md lg:shadow-md">
        <div class="w-full lg:w-3/12 h-full p-6">
            <h3 class="font-bold text-xl">SETTINGS</h3>

            <div class="flex flex-col gap-4 mt-20">
                <button class="flex flex-row gap-4 cursor-pointer" @click="changeModule('edit')"><UserPen />EDIT PROFILE</button>
                <button class="flex flex-row gap-4 cursor-pointer" @click="changeModule('security')"><ShieldCheck />SECURITY</button>
            </div>
        </div>

        <div class="w-full h-full lg:w-9/12 mt-10 lg:mt-0">
            <component :is="currentComponent"></component>
        </div>
    </div>
</template>

<style scoped>
</style>