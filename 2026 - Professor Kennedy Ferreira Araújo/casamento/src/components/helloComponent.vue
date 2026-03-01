<template>
    <section class="hello" id="hello">
      <h1>JENNY & JASON</h1>
      <p>
        On the other hand, we denounce with righteous indignation and dislike men who are so
        beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire.
      </p>
    </section>
</template>
<style scoped>
main .hello {
    text-align: center;

    h1 {
      font-family: 'Aboreto', serif;
      font-size: 9vw;
      margin: 2.5vw;
    }

    p {
      position: relative;
      padding: 12vw 20vw;
      color: white;
      font-family: 'Instrument Serif', serif;
      font-size: 2.3vw;
      overflow: hidden;
      z-index: 1;
    }

    p::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        linear-gradient(rgba(0, 0, 0, 0.566), rgba(0, 0, 0, 0.566)),
        url('@/assets/img/masaaki-komori-NoXUQ54pDac-unsplash.jpg') center/cover no-repeat;
      background-position: 100% 61%;
      filter: blur(3.5px);
      z-index: -1;
      transform: scale(1.1);
    }
  }
</style>
