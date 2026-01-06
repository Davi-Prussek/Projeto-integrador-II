import { ref } from 'vue'
import { defineStore } from 'pinia'

export const showLogin = defineStore('semIdeiaPraNome', () => {
  const control = ref(false);

  return { control }
})
