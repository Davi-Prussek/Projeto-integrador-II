<script setup>
import { addRoom,addFuncionario } from '@/plugins/axios';
import { ref } from 'vue';

const numero = ref('');
const preco = ref('');
const image = ref('');

async function quarto() {
  const dados = {
    numero: numero.value,
    preco: preco.value,
    image: image.value
  }
  numero.value = '';
  preco.value = '';
  image.value = '';
try {
  await addRoom(dados);
  alert("Quarto cadastrado");
} catch (error) {
  alert("Erro ao cadastrar quarto")
  throw error;
}
}

const nome = ref('');
const cargo = ref('');
const email = ref('');
const telefone = ref('');
async function funcionario() {
  const dados = {
    nome: nome.value,
    cargo: cargo.value,
    email: email.value,
    telefone: telefone.value,
  }
  nome.value = '';
  cargo.value = '';
  email.value = '';
  telefone.value = '';
  try {
    await addFuncionario(dados)
      alert("Funcionário cadastrado!");
    } catch (error) {
      alert("Erro ao registrar funcionário!");
      throw error;
    }
  }
</script>
<template>
<body>
<h1>Controle da administração de serviços do hotel</h1>
<div>
<form @submit.prevent="quarto">
<h2>Registrar quartos</h2>
<input type="text" v-model="numero" placeholder="Número do quarto:">
<input type="number" v-model="preco" placeholder="Preço do quarto:">
<input type="url" v-model="image" placeholder="URL da imagem do quarto:">

<button type="submit">Adicionar Quartos</button>
</form>
<form @submit.prevent="">
<h2>Registrar funcionários</h2>
<input type="text" v-model="nome" placeholder="nome:">
<input type="text" v-model="cargo" placeholder="cargo:">
<input type="text" v-model="email" placeholder="email:">
<input type="text" v-model="telefone" placeholder="telefone:">

<button type="submit">Registrar funcionário</button>
</form>
</div>
</body>
</template>
<style scoped>
body {
  text-align: center;
  margin-top: 4vw;
  div {
    display: flex;
    justify-content: center;
    gap: 3vw;
    form {
      flex: 1;
      box-shadow: 0 0 15px rgba(0, 0, 0, .15);
      padding: 2vw 1vw;
    }
  }
}
</style>
