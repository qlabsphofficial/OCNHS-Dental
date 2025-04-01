<script setup>

</script>

<template>
<div class="absolute top-0 left-0 w-full">
  <!-- Header -->
  <div class="flex flex-row justify-between w-full h-20 p-14 main-color">
    <div class="flex flex-row gap-5 h-full items-center">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo1.png" height="90px" width="70px">
      <h3 class="text-white font-bold text-lg">OLONGAPO CITY NATIONAL HIGH SCHOOL DENTAL CLINIC</h3>
    </div>

    <div class="flex h-full items-center">
      <img src="@/assets/Clinic Assets/Dental Clinic images/image/logo2.png" height="90px" width="70px">
    </div>
  </div>

  <!-- Navbar -->
  <div class="flex flex-row justify-end items-center p-8 secondary-color">
    <div class="flex flex-row gap-5">
      <a>HOME</a>
      <a>ABOUT US</a>
      <a>BLOGS</a>
      <a>SERVICES</a>
      <button class="w-20 text-white rounded-sm main-color">LOGIN</button>
    </div>
  </div>

  <!-- Hero -->
  <div class="flex flex-row justify-between items-center h-full w-full">
    <img src="@/assets/Clinic Assets/Dental Clinic images/image/homebg.png" height="100%" width="100%">
    
    <div class="flex flex-col w-8/12">
      <h1 class="text-green-800 text-6xl font-bold">SMILE, LEARN, AND GROW</h1>
      <p class="mt-5 text-lg">Discover the importance of medical care at our school clinic.</p>
    </div>
  </div>

  <!-- Dental Staff -->
  <div class="w-full h-full p-20 overlay-color">
    <h2 class="text-3xl mb-60">DENTAL STAFF</h2>

    <div class="flex flex-row justify-evenly w-full">
      <div class="flex flex-col w-5/12 h-8/12 items-center">
        <div class="flex flex-col items-center justify-center p-30 rounded-md bg-white">
          <div id="about-1" class="bg-black h-100 w-100 rounded-full border-4 border-green-900 negative-marg"></div>
          <h4 class="text-xl font-bold mt-14 mb-5">EMILY CASTILLO-FANCUBERTA, DMD</h4>
          <p>DENTIST II</p>
          <p class="mt-5">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Mollitia iusto aliquid et. Ex hic illum qui non animi unde id dolore?</p>
        </div>
      </div>

      <div class="flex flex-col w-5/12 h-8/12 items-center">
        <div class="flex flex-col items-center justify-center p-30 rounded-md bg-white">
          <div id="about-2" class="bg-black h-100 w-100 rounded-full border-4 border-green-900 negative-marg"></div>
          <h4 class="text-xl font-bold mt-14 mb-5">SHIELA MAE C. DALANGBAYAN</h4>
          <p>DENTAL ASSISTANT</p>
          <p class="mt-5">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Mollitia iusto aliquid et. Ex hic illum qui non animi unde id dolore?</p>
        </div>
      </div>

      <div></div>
    </div>
  </div>

  <!-- About Us -->
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

a {
  cursor: pointer;
}

.negative-marg {
  margin-top: -40%;
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
</style>