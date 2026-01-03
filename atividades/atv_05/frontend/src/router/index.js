import { createRouter, createWebHistory } from 'vue-router'
import homeView from '@/views/homeView.vue'
import reservaView from '@/views/reservaView.vue'
import roomView from '@/views/roomView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HOME",
      component: homeView
    },
    {
      path: "/Reserva",
      name: "Reserva",
      component: reservaView
    },
    {
      path: "/Quartos",
      name: "Quartos",
      component: roomView
    },
  ],
})

export default router
