<template>
    <section class="registry">
      <h2>REGISTRY</h2>
      <div>
        <p>
          QUALQUER COISA ESCRITA ALEATORIAMNETE PORQUE PRECISAVA DE TEXTO PRA ATIVIDADE. FALTOU UM
          POUQUINHO
        </p>
        <button>GO TO REGISTRY</button>
      </div>
    </section>
</template>
<style scoped>
@media (min-width: 800px) {
main .registry {
    width: 100%;
    background:
      linear-gradient(rgba(0, 0, 0, 0.676)), url(@/assets/img/sergey-shmidt-koy6FlCCy5s-unsplash.jpg);
    background-position: 100% 20%;
    background-size: cover;
    background-repeat: no-repeat;
    font-family: 'Aboreto';
    color: white;
    text-align: center;
    padding-top: 13vw;
    padding-bottom: 9vw;
    margin-bottom: 4vw;

    h2 {
      font-size: 3.2vw;
      margin-bottom: 7vw;
    }

    div {
      margin-inline: 28vw;

      p {
        font-size: 1.8vw;
        margin-bottom: 11vw;
      }

      button {
        font-family: 'Aboreto';
        color: white;
        background-color: #756c63;
        border: none;
        border-radius: 36px;
        font-size: 1.6vw;
        padding: 1.45vw;
        width: 100%;
        cursor: pointer;
      }
    }
  }
}
@media (max-width: 800px) {
main .registry {
    width: 100%;
    background:
      linear-gradient(rgba(0, 0, 0, 0.676)), url(@/assets/img/sergey-shmidt-koy6FlCCy5s-unsplash.jpg);
    background-position: 100% 20%;
    background-size: cover;
    background-repeat: no-repeat;
    font-family: 'Aboreto';
    color: white;
    text-align: center;
    padding-top: 13vw;
    padding-bottom: 9vw;
    margin-bottom: 4vw;

    h2 {
      font-size: 8vw;
      margin-bottom: 9vw;
    }

    div {
      margin-inline: 12vw;

      p {
        font-size: 4vw;
        margin-bottom: 11vw;
      }

      button {
        font-family: 'Aboreto';
        color: white;
        background-color: #756c63;
        border: none;
        border-radius: 36px;
        font-size: 3.5vw;
        padding: 2vw;
        width: 100%;
        cursor: pointer;
      }
    }
  }
}
</style>
