import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const user = ref({})
  const medicalHistory = ref({})

  return { user, medicalHistory }
})
