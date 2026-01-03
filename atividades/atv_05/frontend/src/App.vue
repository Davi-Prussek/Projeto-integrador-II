<script setup>
import { RouterView } from 'vue-router';
import headerComponent from './components/headerComponent.vue';
</script>

<template>
<headerComponent/>
<main>
<RouterView/>
</main>
</template>

<style scoped></style>
