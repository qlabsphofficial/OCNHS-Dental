import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useServiceStore = defineStore('store', () => {
  const currentService = ref(0)

  return { currentService }
})
