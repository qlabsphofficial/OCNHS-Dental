<script setup>
import { CalendarView, CalendarViewHeader } from "vue-simple-calendar"
import { ref } from "vue"

import 'vue-simple-calendar/dist/vue-simple-calendar.css'


const showDate = ref(null)

function setShowDate(d) {
      this.showDate = d;
}
</script>

<template>
      <div class="w-11/12 h-11/12">
            <CalendarView :show-date="showDate">
                  <template #header="{ headerProps }">
                          <CalendarViewHeader :header-props @input="setShowDate" />
                  </template>
            </CalendarView>
      </div>
</template>


<style scoped>

</style>