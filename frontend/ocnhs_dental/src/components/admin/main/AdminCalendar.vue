<script setup>
import { CalendarView, CalendarViewHeader } from "vue-simple-calendar"
import { onMounted, ref } from "vue"

import { ScheduleXCalendar } from '@schedule-x/vue'
import {
  createCalendar,
  createViewDay,
  createViewMonthAgenda,
  createViewMonthGrid,
  createViewWeek,
} from '@schedule-x/calendar'
import '@schedule-x/theme-default/dist/index.css'
import { retrieveAllAppointments } from "@/services/AppointmentService"


const currentDate = '2025-04-01'
const viewWeek = createViewWeek()

const calendarApp = createCalendar({
  selectedDate: currentDate,
  views: [viewWeek],
  defaultView: viewWeek.name,
  events: [],
})

onMounted(async() => {
      let allAppointments = await retrieveAllAppointments()
      
      for (let appointment of allAppointments){
            calendarApp.events.set(appointment)
      }
})
</script>

<template>
      <div class="w-11/12 h-11/12 overflow-y-scroll">
            <ScheduleXCalendar :calendar-app="calendarApp" />
      </div>
</template>


<style scoped>

</style>