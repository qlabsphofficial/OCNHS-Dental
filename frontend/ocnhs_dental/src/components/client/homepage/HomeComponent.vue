<script setup>
import { defineProps } from 'vue';

</script>

<template>
<!-- Hero -->
<div class="flex flex-row justify-between items-center h-full w-full">
            <img src="@/assets/Clinic Assets/Dental Clinic images/image/homebg.png" height="100%" width="100%">

            <div class="flex flex-col justify-center items-center w-8/12">
            <h1 class="text-green-800 text-7xl font-bold chewy">SMILE, LEARN, AND GROW</h1>
            <p class="mt-5 text-2xl font-extrabold">Discover the importance of medical care at our school clinic.</p>
            </div>
            </div>

            <!-- Dental Staff -->
            <div class="w-full h-full p-20 overlay-color">
            <h2 class="text-5xl mb-60">DENTAL STAFF</h2>

            <div class="flex flex-row justify-evenly w-full">
            <div class="flex flex-col w-5/12 h-8/12 items-center">
            <div class="flex flex-col items-center justify-center p-30 rounded-md bg-white">
            <div id="about-1" class="bg-black h-100 w-100 rounded-full border-4 border-green-900 negative-marg"></div>
            <h4 class="text-xl font-bold mt-14 mb-5">EMILY CASTILLO-FANCUBERTA, DMD</h4>
            <p>DENTIST II</p>
            <p class="mt-5">Dr. Emily Castillo-Fancuberta is dedicated to promoting oral health education and preventative care for the students of Olongapo City National High School. We believe that early intervention is key to preventing dental problems and ensuring a lifetime of healthy smiles. Our services include regular checkups, cleanings, and educational programs designed to empower students to take charge of their oral hygiene.</p>
            <div>
              <a href="">TEST</a>
              <a href="">TEST</a>
            </div>
            </div>
            </div>

            <div class="flex flex-col w-5/12 h-8/12 items-center">
            <div class="flex flex-col items-center justify-center p-30 rounded-md bg-white">
            <div id="about-2" class="bg-black h-100 w-100 rounded-full border-4 border-green-900 negative-marg"></div>
            <h4 class="text-xl font-bold mt-14 mb-5">SHIELA MAE C. DALANGBAYAN</h4>
            <p>DENTAL ASSISTANT</p>
            <p class="mt-5">Shiela Mae Dalangbayan is dedicated to providing compassionate and efficient support to Dr. Emily Castillo-Fancuberta and our young patients at Olongapo City National High School. She is committed to creating a welcoming and reassuring environment for all students during their dental visits.</p>
            <div>
              <a href="">TEST</a>
              <a href="">TEST</a>
            </div>
            </div>
            </div>

            </div>
            </div>

            <!-- About Us -->
            <div class="w-full p-20">
            <h2 class="text-5xl">ABOUT US</h2>

            <div class="flex flex-row w-full gap-3 mt-20">
            <div class="w-3/12 p-3 border-1 rounded-md">

            </div>

            <div class="w-5/12 p-10 border-black border-1 rounded-md z-10">
            <p>
            Our school dental clinic provides comprehensive, high-quality dental care in a comfortable and friendly environment. 
            We are dedicated to promoting good oral hygiene habits and preventing dental problems among learners, ensuring healthy smiles for a lifetime of learning. 
            Our dentist utilize the latest techniques and technology to deliver gentle and effective treatments, making dental visits a positive experience. 
            We offer a range of services, from routine check-ups and cleanings to restorative treatments and extractions, tailored to meet the unique needs of young patients. 
            We believe that access to quality dental care is essential for a child's overall well-being and academic success, and we are committed to making that a reality for every learner.
            </p>
            </div>

            <div class="w-3/12 p-3 border-1 rounded-md mt-">

            </div>
            </div>
            </div>

            <!-- Appointments -->
            <div class="w-full p-20 overlay-color">
            <h2 class="text-5xl">APPOINTMENTS SCHEDULE</h2>

            <div class="flex flex-row justify-evenly w-full">
            <!-- TODO Calendar -->
            <div class="flex flex-col items-center justify-center w-6/12 p-20">
            </div>

            <div class="flex flex-col items-center justify-center w-6/12 p-20 border-2 rounded-md bg-white">
            <h2 class="text-3xl">CLINIC HOURS</h2>
            <hr>
            <h3>WEEKDAYS</h3>
            <h3>8:00 AM - 5:00 PM</h3>

            <h3 class="text-red-600">Closed during Weekends and Holidays</h3>
            </div>
            </div>
            </div>

            <!-- Blogs -->
            <div class="w-full h-full p-20">
            <h2 class="text-5xl">BLOGS</h2>

            <div class="flex flex-row gap-5 w-full mt-20">
            <div class="flex flex-col items-center justify-center h-full w-3/12 border-1 border-grey-500 rounded-md p-20">
            <div id="blog-1" class="h-60 w-60 rounded-full"></div>
            <p class="mt-5 text-lg">The Proper Way to Brush Your Teeth</p>

            <div id="blog-2" class="h-60 w-60 rounded-full mt-24"></div>
            <p class="mt-5 text-lg">Surprising Causes of Bad Breath</p>
            </div>

            <div class="flex flex-col items-center justify-center h-full w-3/12 border-1 border-grey-500 rounded-md p-20">
            <div id="blog-3" class="h-60 w-60 rounded-full"></div>
            <p class="mt-5 text-lg">How bad oral hygiene can lead to oral cancer and heart problems?</p>

            <div id="blog-4" class="h-60 w-60 rounded-full mt-10"></div>
            <p class="mt-5 text-lg">The relationship between diet and oral health explained</p>
            </div>

            <div class="flex flex-col items-center justify-center h-full w-3/12 border-1 border-grey-500 rounded-md p-20">
            <div id="blog-5" class="h-60 w-60 rounded-full"></div>
            <p class="mt-5 text-lg">8 ways poor oral hygiene can impact your life</p>

            <div id="blog-6" class="h-60 w-60 rounded-full mt-17"></div>
            <p class="mt-5 text-lg">Teaching children how to take care of their teeth</p>
            </div>

            <div class="flex flex-col items-center justify-center h-full w-3/12 border-1 border-grey-500 rounded-md p-20">
            <div id="blog-7" class="h-60 w-60 rounded-full"></div>
            <p class="mt-5 text-lg">Dental Cosmetics</p>

            <div id="blog-8" class="h-60 w-60 rounded-full mt-24"></div>
            <p class="mt-5 text-lg">Dental Surgery</p>
            </div>
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
</style>