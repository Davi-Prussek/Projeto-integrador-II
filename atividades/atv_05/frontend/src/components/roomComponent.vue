<script setup>
import {quartos} from '@/plugins/axios'
import { onMounted, ref } from 'vue';

const listaQuartos = ref([]);

onMounted(async () => {
  try {
    listaQuartos.value = await quartos()
  } catch (error) {
    console.log('Erro ao buscar quartos:', error)
  }
})
</script>
<template>
<ul>
  <li v-for="(quarto, index) in listaQuartos" :key="index" style="max-width: 5vw;">
    <h3>Quarto N°{{ quarto.numero }}</h3>
    <img :src="quarto.img" alt="quarto/image" style="max-width: 100%;">
  </li>
</ul>
</template>
