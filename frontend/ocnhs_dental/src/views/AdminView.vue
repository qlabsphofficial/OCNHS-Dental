<script setup>
import HeaderComponent from '@/components/shared/HeaderComponent.vue';
import AdminNavbar from '@/components/admin/main/AdminNavbar.vue';

// Dynamic Components
import AdminDashboard from '@/components/admin/main/AdminDashboard.vue';
import AdminAppointments from '@/components/admin/main/AdminAppointments.vue';
import AdminCalendar from '@/components/admin/main/AdminCalendar.vue';
import AdminStudentRecord from '@/components/admin/main/AdminStudentRecord.vue';
import AdminAccounts from '@/components/admin/main/AdminAccounts.vue';
import AdminDentalExam from '@/components/admin/main/AdminDentalExam.vue';
import AdminReports from '@/components/admin/main/AdminReports.vue';

import { ref, shallowRef  } from 'vue';
import { useRouter } from 'vue-router';

const currentComponent = shallowRef(null) 
const router = useRouter()

function handleUpdateModule(data){
      switch(data.moduleName) {
            case 'dashboard':
                  currentComponent.value = AdminDashboard
                  break
            case 'appointments':
                  currentComponent.value = AdminAppointments
                  break
            case 'calendar':
                  currentComponent.value = AdminCalendar
                  break
            case 'studentRecord':
                  currentComponent.value = AdminStudentRecord
                  break
            case 'accounts':
                  currentComponent.value = AdminAccounts
                  break
            case 'dentalExam':
                  currentComponent.value = AdminDentalExam
                  break
            case 'reports':
                  currentComponent.value = AdminReports
                  break
      }
}

function attemptLogout() {
      router.push('/')
}
</script>


<template>
      <div class="w-full h-full top-0 left-0 absolute">
            <HeaderComponent />

            <div class="flex flex-row h-11/12 w-full">
                  <AdminNavbar @update-module="handleUpdateModule" @log-out="attemptLogout()" />
                  <div class="flex items-center justify-center w-10/12 h-full">
                        <!-- <div class="flex items-center justify-center absolute">
                              <div>
                                    Test
                              </div>
                        </div> -->
                        <component :is="currentComponent" @view-all-appointments="handleUpdateModule({'moduleName': 'appointments'})"></component>
                  </div>
            </div>
      </div>
</template>

<style scoped>

</style>