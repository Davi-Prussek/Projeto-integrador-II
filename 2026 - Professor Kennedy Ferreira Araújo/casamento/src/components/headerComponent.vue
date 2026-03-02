<template>
  <header>
    <nav>
      <div>
      <h2>J&J</h2>
      <p>June, 23 rd, 2025</p>
    </div>
    <ul>
      <li><p>HOME</p></li>
      <li><p>OUR HISTORY</p></li>
      <li><p>DETAILS</p></li>
      <li><p>RSVP</p></li>
    </ul>
    </nav>
  </header>
</template>
<style scoped>
@media (min-width: 800px) {
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

    h2 {
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

      li p {
        font-size: 3vh;
        font-family: 'Imprima';
        color: white;
        text-decoration: underline;
        }
      }
}
}
@media (max-width: 800px) {
header nav {
    display: flex;
    background-color: #6b6b6b;
    align-items: center;
    padding: 1vw 2vw;
    justify-content: center;
    gap: 0vw;

    div {
      display: flex;
      align-items: center;
      gap: 1.5vw;

      h2 {
        font-size: 6vw;
        color: white;
        text-decoration: none;
        font-family: 'Instrument Serif', serif;
      }

      p {
        text-wrap: nowrap;
        font-size: 2.4vw;
        font-family: 'Instrument Serif', serif;
        color: white;
      }
    }
    ul {
      list-style: none;
      display: flex;
      gap: 2.6vw;
      flex-wrap: nowrap;
      li p {
        text-wrap: nowrap;
        font-size: 3.7vw;
        font-family: 'Imprima';
        color: white;
        text-decoration: underline;
        }
      }
}
}
</style>
