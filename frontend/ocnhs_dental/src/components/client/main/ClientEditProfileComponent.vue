<script setup>
import { ref } from 'vue';

const editingMode = ref(false)
</script>

<template>
    <div class="flex flex-col justify-between lg:justify-start h-full w-full">
        <h2 class="text-2xl font-bold">Edit Profile</h2>

        <div class="w-full flex flex-col gap-6 lg:mt-20">
            <div class="flex flex-col lg:flex-row lg:items-center w-full gap-4 mt-10 lg:mt-0">
                <h4 class="font-bold">NAME:</h4>
                <input type="text" class="border-2 rounded-md p-1" placeholder="First Name" v-model="firstName">
                <input type="text" class="border-2 rounded-md p-1" placeholder="Middle Name" v-model="middleName">
                <input type="text" class="border-2 rounded-md p-1" placeholder="Last Name" v-model="lastName">
                <input type="text" class="border-2 rounded-md p-1" placeholder="Suffix" v-model="suffix">
            </div>

            <div class="flex flex-col lg:flex-row lg:items-center w-full gap-2">
                <h4 class="font-bold">DATE OF BIRTH:</h4>
                <input type="date" class="border-2 rounded-md p-1" v-model="birthDate">
                
                <h4 class="font-bold">AGE:</h4>
                <input type="text" class="border-2 rounded-md p-1" v-model="age">

                <h4 class="font-bold">GENDER:</h4>
                <select class="border-2" v-model="gender">
                        <option value="MALE">MALE</option>
                        <option value="FEMALE">FEMALE</option>
                </select>

                <h4 class="font-bold">BIRTHPLACE:</h4>
                <input type="text" class="border-2 rounded-md p-1 w-full lg:w-6/12" v-model="placeOfBirth">
            </div>

            <div class="flex flex-col lg:flex-row lg:items-center w-full gap-2">
                <h4 class="font-bold">CONTACT NUMBER:</h4>
                <input type="text" class="border-2 rounded-md p-1 w-full lg:w-4/12" v-model="contact">

                <h4 class="font-bold">PARENT / GUARDIAN:</h4>
                <input type="text" class="border-2 rounded-md p-1 w-full lg:w-4/12" v-model="parentName">

                <h4 class="font-bold">ADVISER:</h4>
                <input type="text" class="border-2 rounded-md p-1 w-full lg:w-4/12" v-model="adviserName">
            </div>

            <div class="flex flex-col lg:flex-row lg:items-center w-full gap-2">
                <h4 class="font-bold">ADDRESS:</h4>
                <input type="email" class="border-2 rounded-md p-1 w-full lg:w-1/2" v-model="address">

                <h4 class="font-bold">EMAIL:</h4>
                <input type="email" class="border-2 rounded-md p-1 w-full lg:w-1/2" v-model="email">
            </div>

            <div class="flex flex-col lg:flex-row lg:items-center justify-between w-full gap-4">
                <div class="lg:w-1/3">
                    <h4 class="font-bold">CURRICULUM</h4>
                    <select class="w-full border-2" v-model="curriculum">
                        <option value="BEP">BEP</option>
                        <option value="STE">STE</option>
                        <option value="SPA">SPA</option>
                        <option value="SPS">SPS</option>
                        <option value="SPFL">SPFL</option>
                        <option value="SPJ">SPJ</option>
                        <option value="ICT">ICT</option>
                        <option value="SPED">SPED</option>
                        <option value="ALIVE">ALIVE</option>
                        <option value="OHSP">OHSP</option>
                        <option value="IPED">IPED</option>
                    </select>
                </div>

                <div class="lg:w-1/3">
                    <h4 class="font-bold">GRADE LEVEL</h4>
                    <select class="w-full border-2" v-model="gradeLvl">
                        <option value="GRADE 7">GRADE 7</option>
                        <option value="GRADE 8">GRADE 8</option>
                        <option value="GRADE 9">GRADE 9</option>
                        <option value="GRADE 10">GRADE 10</option>
                        <option value="GRADE 11">GRADE 11</option>
                        <option value="GRADE 12">GRADE 12</option>
                    </select>
                </div>

                <div class="lg:w-1/3">
                    <h4 class="font-bold">SECTION</h4>
                    <select class="w-full border-2" v-model="section">
                          <option value="1">1</option>
                          <option value="2">2</option>
                          <option value="3">3</option>
                          <option value="4">4</option>
                          <option value="5">5</option>
                          <option value="6">6</option>
                          <option value="7">7</option>
                          <option value="8">8</option>
                          <option value="9">9</option>
                          <option value="10">10</option>
                    </select>
                </div>
            </div>
        </div>

        <div class="w-full flex lg:items-center justify-center mt-6 pb-10 lg:pb-0">
            <button v-if="!editingMode" @click="() => { editingMode = true }" class="w-3/12 border-2 p-2">EDIT</button>

            <div v-else class="w-full flex flex-row gap-4 justify-center items-center">
                <button class="w-3/12 border-2 p-2">SAVE</button>
                <button @click="() => { editingMode = false }" class="w-3/12 border-2 p-2">CANCEL</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>