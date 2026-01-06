<script setup>
import { login } from '@/plugins/axios';
import { ref } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faEye, faEyeSlash,faXmark } from '@fortawesome/free-solid-svg-icons'
import { showLogin } from '@/stores/login';

const show = showLogin();
const nome = ref('');
const senha = ref('');

async function logar() {
  try {
    await login(nome.value, senha.value);
    alert("Usuário logado com sucesso!");
    show.control = !show.control;
  } catch {
    alert("Erro, usuário ou senha não encontrados!")
  }
}

const password = ref('password');
function verDesver() {
  if (password.value == 'password') {
    password.value = 'text';
  } else {
    password.value = 'password'
  }
}
</script>
<template>
  <form @submit.prevent="logar">
    <div class="firtLine">
    <p>LOGIN</p>
    <button type="button" @click="show.control = !show.control" class="close"><FontAwesomeIcon :icon="faXmark" style="color: #4141de; font-size: 1.5vw;" /></button>
    </div>
    <div>
      <div>
        <input type="text" v-model="nome" placeholder="Nome: ">
        <div class="senha">
          <input :type="password" v-model="senha" placeholder="Senha: ">
          <button type="button" @click="verDesver">
            <FontAwesomeIcon :icon="password === 'password' ? faEye : faEyeSlash" />
          </button>
        </div>
      </div>
      <button class="submit" type="submit">Logar</button>
    </div>
  </form>
</template>
<style scoped>
form {
  position: fixed;
  right: 0;
  top: 0;
  bottom: 0;
  left: 0;
  width: fit-content;
  margin: auto;
  height: fit-content;
  background: white;
  border-radius: 14px;
  padding-inline: 1.5vw;
  padding-bottom: 1.5vw;
  box-shadow: 0 0 15px rgba(0, 0, 0, .15);
  display: flex;
  flex-direction: column;
  gap: 2vw;
  .firtLine {
    display: flex;
    flex-direction: row;
    border-bottom: 0.2px solid rgb(65, 65, 222);
    p {
      font-size: 2vw;
    }
    .close {
      border: none;
      border-radius: 5px;
      background: transparent;
      font-size: 1.2vw;
      cursor: pointer;
      margin-left: auto;
      color: rgb(65, 65, 222);
    }
  }

  div {
    display: flex;
    flex-direction: column;
    gap: 4vw;

    div {
      display: flex;
      flex-direction: column;
      gap: 1.7vw;

      input {
        font-size: 1.1vw;
        border: none;
        padding: 0.3vw 0.4vw;
        background-color: rgb(245, 245, 245);
        border-radius: 4px;
      }

      .senha {
        display: flex;
        gap: 0.5vw;
        flex-direction: row;


        input {
          flex: 1;
          padding: 0.5vw;
          font-size: 1.1vw;
          border: none;
          border-radius: 5px;
        }

        button {
          border: none;
          background-color: rgb(65, 65, 222);
          color: white;
          border-radius: 5px;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 0 0.6vw;
        }
      }
    }

    .submit {
      background-color: rgb(65, 65, 222);
      color: white;
      border: none;
      border-radius: 12px;
      font-size: 1.2vw;
      padding: 0.5vw 0vw;
      margin-inline: 2vw;
    }
  }
}
</style>
