<script setup>
import { useBlogStore } from '@/stores/blogs';
import { useRouter } from 'vue-router';
import { CalendarView, CalendarViewHeader } from "vue-simple-calendar"
import { ref, onMounted } from "vue"
import { ScheduleXCalendar } from '@schedule-x/vue'
import {
  createCalendar,
  createViewDay,
  createViewMonthAgenda,
  createViewMonthGrid,
  createViewWeek,
} from '@schedule-x/calendar'
import '@schedule-x/theme-default/dist/index.css'
import { createEventsServicePlugin } from '@schedule-x/events-service'

import { Facebook } from 'lucide-vue-next';
import { Mail } from 'lucide-vue-next';
import { retrieveAllAppointments } from '@/services/AppointmentService';

const blogStore = useBlogStore()
const router = useRouter()
const currentDate = '2025-04-01'
const viewWeek = createViewWeek()
 
// Do not use a ref here, as the calendar instance is not reactive, and doing so might cause issues
// For updating events, use the events service plugin
const eventsServicePlugin = createEventsServicePlugin();

const calendarApp = createCalendar({
  selectedDate: currentDate,
  views: [viewWeek],
  defaultView: viewWeek.name,
  events: [],
}, [eventsServicePlugin])

onMounted(async() => {
      let allAppointments = await retrieveAllAppointments()

      let index = 1

      for (let appointment of allAppointments){
            calendarApp.eventsService.add({
                  title: `${appointment.appointment_type}`,
                  description: `${appointment.student_info.firstname} ${appointment.student_info.lastname}`,
                  start: `${appointment.appointment_datetime.substring(0, 10)} ${appointment.appointment_datetime.substring(11, 16)}`,
                  end: `${appointment.appointment_datetime.substring(0, 10)} ${appointment.appointment_datetime.substring(11, 16)}`,
                  id: index
            })

            index += 1
      }
})
</script>

<template>
<!-- Hero -->
<!-- <div class="flex lg:flex-row sm:flex-col justify-evenly items-evenly h-full w-full"> -->
<div class="flex lg:flex-row sm:flex-col justify-evenly items-evenly h-full w-full">
  <img src="@/assets/Clinic Assets/Dental Clinic images/image/homebg.png" height="100%" width="100%" class="hidden lg:block">

  <div class="flex flex-col justify-center items-center w-full pt-20 pb-20 lg:p-0 lg:w-8/12">
    <h1 class="text-green-800 text-6xl lg:text-8xl font-bold chewy">SMILE, LEARN, AND GROW</h1>
    <p class="mt-5 lg:text-2xl text-lg lg:font-extrabold">Discover the importance of medical care at our school clinic.</p>
  </div>
</div>

<!-- Dental Staff -->
<div class="flex flex-col items-center lg:items-start w-full h-full p-10 lg:p-20 overlay-color">
  <h2 class="text-5xl lg:mb-60 font-bold">DENTAL STAFF</h2>

  <div class="flex flex-col lg:flex-row items-center justify-evenly w-full">
    <div class="flex flex-col w-11/12 lg:w-5/12 h-8/12 items-center mt-10 lg:mt-0">
      <div class="flex flex-col items-center justify-center p-30 rounded-md bg-white h-180">
        <div id="about-1" class="bg-black rounded-full border-4 border-green-900 lg:h-74 lg:w-74 negative-marg hidden lg:block"></div>
        
        <div class="flex flex-col items-center justify-center">
          <h4 class="text-2xl font-bold lg:mt-14 lg:mb-5">EMILY CASTILLO-FANCUBERTA, DMD</h4>
          <p>DENTIST II</p>
          <p class="mt-5">Dr. Emily Castillo-Fancuberta is dedicated to promoting oral health education and preventative care for the students of Olongapo City National High School. We believe that early intervention is key to preventing dental problems and ensuring a lifetime of healthy smiles. Our services include regular checkups, cleanings, and educational programs designed to empower students to take charge of their oral hygiene.</p>
          <div class="flex flex-row gap-2 items-center justify-center mt-5">
            <a href="https://www.facebook.com/share/1Bf7QRoqEo/"><Facebook /></a>
            <a href="castillodmd@yahoo.com"><Mail /></a>
          </div>
        </div>
      </div>
    </div>

    <div class="flex flex-col w-11/12 lg:w-5/12 h-8/12 items-center mt-20 lg:mt-0">
    <div class="flex flex-col items-center justify-center p-30 rounded-md bg-white h-180">
    <div id="about-2" class="bg-black rounded-full border-4 border-green-900 lg:h-74 lg:w-74 negative-marg hidden lg:block"></div>
    <h4 class="text-xl font-bold mt-14 mb-5">SHIELA MAE C. DALANGBAYAN</h4>
    <p>DENTAL ASSISTANT</p>
    <p class="mt-5">Shiela Mae Dalangbayan is dedicated to providing compassionate and efficient support to Dr. Emily Castillo-Fancuberta and our young patients at Olongapo City National High School. She is committed to creating a welcoming and reassuring environment for all students during their dental visits.</p>
    <div class="flex flex-row gap-2 items-center justify-center mt-5">
      <a href="https://www.facebook.com/ShielaMaeDalangbayan"><Facebook /></a>
      <a href="shielamaedalangbayan.smd@gmail.com"><Mail /></a>
    </div>
    </div>
    </div>

  </div>
</div>

    <!-- About Us -->
    <div class="flex flex-col items-center justify-center lg:justify-start lg:items-start lg:flex-none w-full pt-10 lg:p-20">
      <h2 class="text-5xl font-bold">ABOUT US</h2>

      <div class="flex flex-row justify-center w-full gap-3 mt-5 lg:mt-20">
        <div class="flex flex-col gap-4 justify-center items-center w-3/12 p-3 border-1 rounded-md hidden lg:block">
          <div id="info-1" class="h-60 w-60 rounded-full border-4"></div>
          <div id="info-2" class="h-60 w-60 rounded-full border-4"></div>
        </div>

        <div class="flex flex-col justify-center items-center w-full lg:w-5/12 p-10 border-black lg:border-1 rounded-md z-10">
          <p>
          Our school dental clinic provides comprehensive, high-quality dental care in a comfortable and friendly environment. 
          We are dedicated to promoting good oral hygiene habits and preventing dental problems among learners, ensuring healthy smiles for a lifetime of learning. 
          </p>

          <p class="mt-10">
            Our dentist utilize the latest techniques and technology to deliver gentle and effective treatments, making dental visits a positive experience. 
          We offer a range of services, from routine check-ups and cleanings to restorative treatments and extractions, tailored to meet the unique needs of young patients. 
          We believe that access to quality dental care is essential for a child's overall well-being and academic success, and we are committed to making that a reality for every learner.
          </p>
        </div>

        <div class="flex flex-col gap-4 justify-center items-center w-3/12 p-3 border-1 rounded-md hidden lg:block">
          <div id="info-3" class="h-60 w-60 rounded-full border-4"></div>
          <div id="info-4" class="h-60 w-60 rounded-full border-4"></div>
        </div>
    </div>
    </div>

    <!-- Appointments -->
    <div class="flex flex-col items-center justify-center lg:items-start lg:justify-start lg:flex-none w-full p-5 lg:p-20 overlay-color">
      <h2 class="text-4xl lg:text-5xl font-bold text-center">APPOINTMENTS SCHEDULE</h2>

      <div class="flex flex-col items-center justify-center lg:flex-row justify-evenly w-full mt-10 gap-4">
        <div class="flex flex-col w-full lg:w-6/12 h-200 overflow-y-scroll lg:p-10 bg-white rounded-md border-2">
          <ScheduleXCalendar :calendar-app="calendarApp" />
        </div>

        <div class="flex flex-col items-center justify-center w-full lg:w-6/12 p-20 border-2 rounded-md bg-white">
          <h2 class="text-3xl font-bold">CLINIC HOURS</h2>
          <hr>
          <h3>WEEKDAYS</h3>
          <h3>8:00 AM - 5:00 PM</h3>

          <h3 class="text-red-600">Closed during Weekends and Holidays</h3>
        </div>
      </div>
    </div>

    <!-- Blogs -->
    <div class="w-full h-full mt-20 lg:mt-0 p-10 lg:p-20">
    <h2 class="text-5xl font-bold text-center lg:text-left">BLOGS</h2>

    <div class="flex flex-col lg:flex-row gap-5 w-full mt-20">
      <div class="flex flex-col items-center justify-center h-full lg:w-3/12 border-1 border-grey-500 rounded-md p-22">
        <div id="blog-1" class="h-60 w-60 rounded-full" @click="() => { blogStore.blog = 1; router.push('/blog') }"></div>
        <p class="mt-5 text-lg">The Proper Way to Brush Your Teeth</p>

        <div id="blog-2" class="h-60 w-60 rounded-full mt-24" @click="() => { blogStore.blog = 2; router.push('/blog') }"></div>
        <p class="mt-5 text-lg">Surprising Causes of Bad Breath</p>
      </div>

      <div class="flex flex-col items-center justify-center h-full lg:w-3/12 border-1 border-grey-500 rounded-md p-23">
        <div id="blog-3" class="h-60 w-60 rounded-full" @click="() => { blogStore.blog = 3; router.push('/blog') }"></div>
        <p class="mt-5 text-lg">How bad oral hygiene can lead to oral cancer and heart problems?</p>

        <div id="blog-4" class="h-60 w-60 rounded-full mt-10" @click="() => { blogStore.blog = 4; router.push('/blog') }"></div>
        <p class="mt-5 text-lg">The relationship between diet and oral health explained</p>
      </div>

      <div class="flex flex-col items-center justify-center h-full lg:w-3/12 border-1 border-grey-500 rounded-md p-23">
        <div id="blog-5" class="h-60 w-60 rounded-full" @click="() => { blogStore.blog = 5; router.push('/blog') }"></div>
        <p class="mt-5 text-lg">8 ways poor oral hygiene can impact your life</p>

        <div id="blog-6" class="h-60 w-60 rounded-full mt-17" @click="() => { blogStore.blog = 6; router.push('/blog') }"></div>
        <p class="mt-5 text-lg">Teaching children how to take care of their teeth</p>
      </div>

      <div class="flex flex-col items-center justify-center h-full lg:w-3/12 border-1 border-grey-500 rounded-md p-27">
        <div id="blog-7" class="h-60 w-60 rounded-full" @click="() => { blogStore.blog = 7; router.push('/blog') }"></div>
        <p class="mt-5 text-lg">Dental Cosmetics</p>

        <div id="blog-8" class="h-60 w-60 rounded-full mt-24" @click="() => { blogStore.blog = 8; router.push('/blog') }"></div>
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

.hero-negative-marg {
  margin-left: -30%;
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

#info-1 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/cleaning.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#info-2 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/flouride.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#info-3 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/restoration.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

#info-4 {
  background-image: url('@/assets/Clinic Assets/Dental Clinic images/image/extraction.jpg');
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