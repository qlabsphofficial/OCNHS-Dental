import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useBlogStore = defineStore('blog', () => {
  const currentBlog = ref(0)

  return { currentBlog }
})
