<script setup>
import { ref } from 'vue';

const user = JSON.parse(sessionStorage.getItem('user'))

const name = ref('');
const dateOfBirth = ref('');
const parentGuardian = ref('');
const adviser = ref('');
const gender = ref('');
const age = ref('');
const contactNumber = ref('');
const address = ref('');
const curriculum = ref('');
const gradeLevel = ref('');
const section = ref('');

name.value = `${user.firstname} ${user.middlename} ${user.lastname}`
dateOfBirth.value = user.dateofbirth
parentGuardian.value = user.parent_guardian_name
adviser.value = user.adviser_name
gender.value = user.gender
age.value = user.age
contactNumber.value = user.contact_no
address.value = user.address
curriculum.value = user.curriculum
gradeLevel.value = user.grade_level
section.value = user.section


// receive data from the user here
// Use a store
</script>

<template>
      <div class="flex flex-col justify-center h-8/12 w-8/12 gap-10 p-20 border-2 rounded-md">
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Name</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="name" disabled>
            </div>
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Date of Birth</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="dateOfBirth" disabled>
            </div>
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Parent / Guardian</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="parentGuardian" disabled>
            </div>
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Adviser</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="adviser" disabled>
            </div>
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Gender</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="gender" disabled>
            </div>
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Age</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="age" disabled>
            </div>
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Contact Number</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="contactNumber" disabled>
            </div>
            <div class="flex flex-row justify-between w-full gap-5">
                  <h4>Address</h4>
                  <input type="text" class="w-10/12 p-2 bg-gray-300 rounded-sm" v-model="address" disabled>
            </div>
            <div class="flex flex-row justify-between">
                  <div class="flex flex-row gap-5">
                        <h4>Curriculum</h4>
                        <input type="text" v-model="curriculum" disabled>
                  </div>

                  <div class="flex flex-row gap-5">
                        <h4>Grade Level</h4>
                        <input type="text" v-model="gradeLevel" disabled>
                  </div>

                  <div class="flex flex-row gap-5">
                        <h4>Section</h4>
                        <input type="text" v-model="section" disabled>
                  </div>
            </div>
      </div>
</template>

<style scoped>

</style>