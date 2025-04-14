<script setup>
import { useRouter } from 'vue-router';
import { TriangleAlert } from 'lucide-vue-next';

const router = useRouter()
</script>

<template>
      <div id="container" class="flex items-center justify-center absolute top-0 left-0">
            <div class="flex flex-col justify-center items-center bg-white rounded-md shadow-md p-10">
                  <div class="flex flex-col justify-center items-center">
                        <TriangleAlert />
                        <h1 class="text-2xl font-bold">LOG OUT</h1>
                  </div>

                  <p>Are you sure you want to log out?</p>

                  <div class="flex flex-col gap-4 w-full">
                        <button class="w-full text-white bg-red-500 cursor-pointer" @click="() => { router.push('/') }">LOG OUT</button>
                        <button class="w-full bg-gray-200 cursor-pointer">CANCEL</button>
                  </div>
            </div>
      </div>
</template>

<style scoped>
#container {
      background-color: rgba(000, 000, 000, .4);
}
</style>