<template>
  <header>
    <ul>
      <li>
        <div>
          <h2>J&J</h2>
          <p>June, 23 rd, 2025</p>
        </div>
      </li>
      <li>
        <p>HOME</p>
      </li>
      <li>
        <p>OUR HISTORY</p>
      </li>
      <li>
        <p>DETAILS</p>
      </li>
      <li>
        <p>RSVP</p>
      </li>
    </ul>
  </header>
</template>
<style scoped lang="css">
@media (min-width: 800px) {
  header {
    background-color: #6b6b6b;
    padding: 1vw 3vw;
    ul {
      list-style: none;
      display: flex;
      gap: 4vw;
      flex-wrap: wrap;
      align-items: center;

      li {
        div {
          display: flex;
          align-items: center;
          gap: 1.5vw;
          h2 {
            margin: 0;
            padding: 0;
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

        p {
          margin: 0;
          padding: 0;
          font-size: 2vw;
          font-family: 'Imprima';
          color: white;
          text-decoration: underline;
        }
      }
      li:first-child {
        margin-right: auto;
      }
    }
  }
}

@media (max-width: 800px) {
  header {
    display: flex;
    background-color: #6b6b6b;
    align-items: center;
    padding: 1vw 0;

    ul {
      margin: 0;
      padding: 0 4vw;
      width: 100%;
      list-style: none;
      display: flex;
      align-items: center;
      flex-wrap: nowrap;
      justify-content: space-between;
      gap: 4vw;

      li {
        div {
          display: flex;
          align-items: center;
          gap: 1.5vw;

          h2 {
            font-weight: lighter;
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

        p {
          text-wrap: nowrap;
          font-size: 3.8vw;
          font-family: 'Imprima';
          color: white;
          text-decoration: underline;
        }
      }

      li:first-child {
        padding-right: 2vw;
      }
    }
  }
}
</style>
