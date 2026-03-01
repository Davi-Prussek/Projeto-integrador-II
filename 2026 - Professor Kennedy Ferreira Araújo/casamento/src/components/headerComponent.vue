<template>
  <header>
    <nav>
      <div>
      <a href="/">J&J</a>
      <p>June, 23 rd, 2025</p>
    </div>
    <ul>
      <li><a href="#hello">HOME</a></li>
      <li><a href="#quadros">OUR HISTORY</a></li>
      <li><a href="#quadros">DETAILS</a></li>
      <li><a href="#quadros">RSVP</a></li>
    </ul>
    </nav>
  </header>
</template>
<style scoped>
header nav {
  display: flex;
  justify-content: space-between;
  background-color: #6b6b6b;
  align-items: center;
  padding: 1vw 3vw;

  div {
    display: flex;
    align-items: center;
    gap: 1.5vw;

    a {
      font-size: 3.5vw;
      color: white;
      text-decoration: none;
      font-family: 'Instrument Serif', serif;
    }

    p {
      font-size: 1.2vw;
      font-family: 'Instrument Serif', serif;
      color: white;
    }
  }

  ul {
    list-style: none;
    display: flex;
    gap: 4vw;
    flex-wrap: wrap;

    li a {
      font-size: 3vh;
      font-family: 'Imprima';
      color: white;
      }
    }
  }
</style>
