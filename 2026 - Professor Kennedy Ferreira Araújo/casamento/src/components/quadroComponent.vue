<template>
  <section class="quadros" id="quadros">
    <ul>
      <li class="quadro-I">
        <h3>OUR STORY</h3>
      </li>
      <li class="quadro-II">
        <h3>the details</h3>
      </li>
      <li class="quadro-III">
        <h3>RSVP</h3>
      </li>
      <li class="quadro-IV">
        <h3>REGISTRY</h3>
      </li>
    </ul>
  </section>
</template>
<style scoped>
@media (min-width: 800px) {
main .quadros {
  ul {
    margin: 0;
    padding: 0;
    color: white;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 5vw;
    text-align: center;
    list-style: none;
    margin-bottom: 3vw;
    padding-top: 3.7vw;

    .quadro-I {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)),
        url(@/assets/img/jose-luis-cofre-io0vRyV-3-U-unsplash.jpg);
      background-size: cover;
      background-position: 100% 48%;
    }

    .quadro-II {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)), url(@/assets/img/anh-nguyen-kcA-c3f_3FE-unsplash.jpg);
      background-size: cover;
      background-position: 100% 55%;
    }

    .quadro-III {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)), url(@/assets/img/george-filippopoulos-vH6qVnY-z0c-unsplash.jpg);
      background-size: cover;
      background-position: 100% 5%;
    }

    .quadro-IV {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)), url(@/assets/img/han-chenxu-YdAqiUkUoWA-unsplash.jpg);
      background-size: cover;
      background-position: 100% 85%;
    }

    li {
      background-position: 100% 60%;
      border-radius: 24px;
      font-family: 'Aboreto';
      width: 40vw;
      align-content: center;
      height: 35vw;
      text-decoration: underline;
      font-size: 2.5vw;
    }
  }
}
}
@media (max-width:800px) {
main .quadros {
  ul {
    color: white;
    display: flex;
    flex-direction: column;
    padding-inline: 6vw;
    gap: 7vw;
    text-align: center;
    list-style: none;
    margin-bottom: 6vw;
    padding-top: 3.7vw;
    li {
      height: 85vw;
      background-position: 100% 60%;
      border-radius: 18px;
      font-family: 'Aboreto';
      align-content: center;
      text-decoration: underline;
      font-size: 6vw;
    }
    .quadro-I {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)),
        url(@/assets/img/jose-luis-cofre-io0vRyV-3-U-unsplash.jpg);
      background-size: cover;
      background-position: 100% 48%;
    }

    .quadro-II {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)), url(@/assets/img/anh-nguyen-kcA-c3f_3FE-unsplash.jpg);
      background-size: cover;
      background-position: 100% 55%;
    }

    .quadro-III {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)), url(@/assets/img/george-filippopoulos-vH6qVnY-z0c-unsplash.jpg);
      background-size: cover;
      background-position: 100% 5%;
    }

    .quadro-IV {
      background:
        linear-gradient(rgba(0, 0, 0, 0.578)), url(@/assets/img/han-chenxu-YdAqiUkUoWA-unsplash.jpg);
      background-size: cover;
      background-position: 100% 85%;
    }
  }
}
}
</style>
