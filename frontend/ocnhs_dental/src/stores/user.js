import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const user = ref({})
  const medicalHistoryExists = ref(false)

  return { user, medicalHistoryExists }
})
