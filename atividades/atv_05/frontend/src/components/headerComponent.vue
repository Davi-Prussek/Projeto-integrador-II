<script setup>
import { RouterLink, useRouter } from 'vue-router'
import formComponent from './formComponent.vue'
import { showLogin } from '@/stores/login'

const router = useRouter()
const routes = router.getRoutes()
const show = showLogin()
</script>


<template>
<header class="header">
  <nav>
    <RouterLink to="/" class="home">HOME</RouterLink>
    <div>
    <RouterLink v-for="(rota, index) in routes.slice(1, routes.length)" :key="index" :to=" rota.path">
        {{ rota.name }}
    </RouterLink>
    <button class="login" @click="show.control = !show.control">LOGIN</button>
  </div>
</nav>
<formComponent v-if="show.control"/>
</header>
</template>
<style scoped>
.header {
  .login {
    border: none;
    background-color: transparent;
    font-size: 1.8vw;
    color: rgb(65, 65, 222);
    font-family: 'Times New Roman', Times, serif;
    font-weight: bolder;
    cursor: pointer;
  }
  nav {
  margin-inline: 4vw;
  margin-top: 1vw;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 1.8vw;
  div {
    display: flex;
    gap: 2.5vw;
  }
  a {
    cursor: pointer;
    text-decoration: none;
    color: black;
  }
  .home {
    font-size: 2.3vw;
    font-weight: bolder;
  }
}
}
</style>
