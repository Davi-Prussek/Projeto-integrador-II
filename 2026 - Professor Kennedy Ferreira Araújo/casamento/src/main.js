import { createApp } from 'vue'
import { createPinia } from 'pinia'

import '@fontsource/instrument-serif'
import '@fontsource/aboreto'
import '@fontsource/imprima'
import '@/assets/main.css'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
