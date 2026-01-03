<script setup>
import { RouterLink, useRouter } from 'vue-router';
const router = useRouter()
const routes = router.getRoutes()
</script>

<template>
<header class="header">
  <nav>
    <RouterLink to="/" class="home">HOME</RouterLink>
    <div>
    <RouterLink v-for="(rota, index) in routes.slice(1, routes.length)" :key="index" :to=" rota.path">
        {{ rota.name }}
    </RouterLink>
    </div>
  </nav>
</header>
</template>
<style scoped>
.header nav {
  margin-inline: 4vw;
  margin-top: 1.5vw;
  display: flex;
  justify-content: space-between;
  font-size: 2vw;
  div {
    display: flex;
    gap: 2.5vw;
  }
  a {
    text-decoration: none;
    color: black;
  }
  .home {
    font-size: 3vw;
    font-weight: bolder;
  }
}
</style>
