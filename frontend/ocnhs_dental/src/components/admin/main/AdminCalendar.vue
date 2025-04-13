<script setup>
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

import { createEventsServicePlugin } from '@schedule-x/events-service'
 
const eventsServicePlugin = createEventsServicePlugin();


const currentDate = '2025-04-01'
const viewWeek = createViewWeek()

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
      <div class="w-11/12 h-11/12 overflow-y-scroll">
            <ScheduleXCalendar :calendar-app="calendarApp" />
      </div>
</template>


<style scoped>

</style>