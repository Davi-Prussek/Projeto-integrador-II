<template>
    <section class="information">
      <img src="@/assets/img/johnson-U6Q6zVDgmSs-unsplash.jpg" alt="imagem de casa americana"/>
      <div>
          <div>
            <h3>LOCAL: RUA DOS BOBOS N°43</h3>
          <h3>HORÁRIO: 19:00</h3>
          </div>
        <p>ESPERO QUE TODOS POSSAM VIR PARA PRESTIGIAR ESSE MOMENTO.</p>
      </div>
    </section>
</template>
<style scoped>
@media (min-width: 800px) {
main .information {
    display: flex;
    justify-content: center;
    padding-inline: 8vw;
    gap: 5vw;
    margin-bottom: 6vw;
    img {
      flex: 1;
      width: 40%;
      height: 41vw;
      border-radius: 24px;
    }
    div {
      flex: 1;
      width: 40%;
      display: flex;
      justify-content: space-around;
      flex-direction: column;
      font-size: 2.2vw;
      font-family: 'Aboreto';
      div {
        width: 100%;
      }
    }
  }
}
@media (max-width: 800px) {
main .information {
    display: flex;
    justify-content: center;
    padding-inline: 6vw;
    gap: 5vw;
    margin-bottom: 10vw;
    img {
      width: 55%;
      height: 55vw;
      border-radius: 14px;
    }
    div {
      width: 40%;
      display: flex;
      justify-content: space-around;
      flex-direction: column;
      font-size: 3vw;
      font-family: 'Aboreto';
      p {
        text-align: center;
      }
    div {
      width: 100%;
      display: flex;
      flex-direction: column-reverse;
    }
    }
  }
}
</style>

