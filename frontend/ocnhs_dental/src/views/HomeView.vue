<script setup>
import HomeComponent from '@/components/client/homepage/HomeComponent.vue';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useServiceStore } from '@/stores/services';

const router = useRouter()
const servicesVisible = ref(false)
const serviceStore = useServiceStore()

function accessService(service){
  serviceStore.currentService = service
  router.push('/service')
}
</script>

<template>
<div class="absolute top-0 left-0 w-full">
  <!-- Header -->
  <div id="home" class="flex flex-row justify-between w-full h-20 p-2 lg:p-16 main-color">
    <div class="flex flex-row gap-5 h-full items-center">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="120px" width="100px" class="hidden lg:block">
      <h3 class="text-white sm:font-bold text-xs lg:text-lg">OLONGAPO CITY NATIONAL HIGH SCHOOL DENTAL CLINIC</h3>
    </div>

    <div class="flex h-full items-center">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="120px" width="100px" class="hidden lg:block">
    </div>
  </div>

  <!-- Navbar -->
  <div class="flex flex-row lg:justify-end items-center p-2 lg:p-8 secondary-color">
    <div class="flex flex-row gap-2 lg:gap-5 footer-links-2">
      <a class="text-sm lg:text-lg">HOME</a>
      <a class="text-sm lg:text-lg" @click="() => { skip = 'about' } ">ABOUT US</a>
      <a class="text-sm lg:text-lg" @click="() => { skip = 'blogs' } ">BLOGS</a>
      <div class="flex flex-col">
        <a class="text-sm lg:text-lg" @click="() => { servicesVisible = !servicesVisible }">SERVICES</a>

        <div v-if="servicesVisible" class="flex flex-col items-start justify-start absolute top-30 lg:top-50 border-2 p-4 lg:p-6 w-8/12 lg:w-2/12 bg-white negative-marg-left">
          <button @click="accessService(1)" class="text-sm lg:text-lg">FLOURIDE APPLICATION</button>
          <button @click="accessService(2)" class="text-sm lg:text-lg">ORAL PROPHYLAXIS/CLEANING</button>
          <button @click="accessService(3)" class="text-sm lg:text-lg">RESTORATION/PASTA</button>
          <button @click="accessService(4)" class="text-sm lg:text-lg">EXTRACTION/BUNOT</button>
        </div>
      </div>
      <button class="w-20 text-white text-sm lg:text-lg rounded-sm main-color" @click="() => { router.push('/login') }">LOGIN</button>
    </div>
  </div>

  <HomeComponent/>

  <!-- Footer -->
  <div class="flex flex-col lg:flex-row justify-evenly items-center h-full w-full overlay-color-2 p-10">
    <div>
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="240px" width="240px">
    </div>

    <div class="w-full text-md lg:w-4/12 lg:text-lg mt-10 lg:mt-0">
      <h4>OLONGAPO CITY NATIONAL HIGH SCHOOL</h4>
      <p>Address:</p>
      <p>Rizal Av. Cor 14th St. East  Tapinac, Olongapo City</p>
      <p>Contact Details: </p>
      <p>(047) 222-2568/(047) 603-0570/ (+63) 920-905-8815</p>
      <p>Email Address:</p>
      <p>olongapo.city@deped.gov.ph</p>
      <p>ocnhsdentalpage@gmail.com</p>
    </div>

    <div class="flex flex-col w-full lg:w-4/12 mt-10 lg:mt-0 footer-links-2">
      <p>DEPED QUICK LINKS</p>
      <a>DepEd Central Office</a>
      <a>DepEd Regional Office III</a>
      <a>Civil Service Commission</a>
      <a>Department of Budget & Management</a>
      <a>Commission on Audit</a>
      <a>PAGASA</a>
    </div>

    <div class="flex flex-col w-full lg:w-4/12 mt-10 lg:mt-0 footer-links-2">
      <p>DEPED PORTALS</p>
      <a>Enhanced Basic Education</a>
      <a>Information System (EBEIS)</a>
      <a>Learner Information System (LIS)</a>
      <a>Learning Resources Management</a>
      <a>and Development System (LRMDS)</a>
      <a>Program Management Information</a>
      <a>System (PMIS)</a>
      <a>Enterprise Human Resources</a>
      <a>Information System (EHRIS)</a>
      <a>WASH in School System (WINS)</a>
    </div>

    <div>
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="240px" width="240px" class="mt-10 lg:mt-0">
    </div>
  </div>

  <!-- Footer 2 -->
  <div class="flex flex-col lg:flex-row justify-evenly items-evenly h-full w-full overlay-color p-10">
    <div class="flex flex-col justify-center items-center lg:items-start w-full lg:w-auto">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo3.png" height="240px" width="240px">
    </div>

    <div class="flex flex-col justify-center w-full mt-10 lg:mt-0 lg:w-3/12 text-white">
      <h4>REPUBLIC OF THE PHILIPPINES</h4>
      <p>All content is in the public domain unless otherwise stated.</p>
    </div>

    <div class="flex flex-col justify-center w-full mt-10 lg:mt-0 lg:w-3/12 text-white">
      <p>ABOUT GOVPH</p>
      <p>
        Learn more about the Philippine
        government, its structure, how
        government works and the people
        behind it.
      </p>
      <p>GOV.PH</p>
      <p>Open Data Portal</p>
      <p>Official Gazette</p>
    </div>

    <div class="flex flex-col w-full mt-10 lg:mt-0 lg:w-3/12 footer-links-1">
      <a>Office of the President</a>
      <a>Office of the Vice President</a>
      <a>Senate of the Philippines</a>
      <a>House of Representatives</a>
      <a>Supreme Court</a>
      <a>Court of Appeals</a>
      <a>Sandiganbayan</a>
    </div>
  </div>

  <div class="flex justify-center items-center w-full main-color">
    <p class="text-white">2025 All Rights Reserved.</p>
  </div>
</div>
</template>

<style scoped>
/* RESPONSIVE DESIGN */
@media (max-width: 768px) {

} 

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

a {
  cursor: pointer;
}

.negative-marg {
  margin-top: -40%;
}

.negative-marg-left {
  margin-left: -15%;
}

#about-1 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/dentist-mod.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#about-2 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/assistant-mod.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-1 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/1.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-2 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/2.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-3 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/3.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-4 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/4.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-5 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/5.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-6 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/6.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-7 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/7.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#blog-8 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/blog/8.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

.footer-links-1 a {
  color: white;
}

.footer-links-2 a {
  color: black;
}
</style>