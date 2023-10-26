<script setup>
defineProps({
  data: Number,
  title: String,
  description: String,
  title_gradient: String
})
</script>

<template>
  <article class="card">
    <h1 :class=title_gradient>{{ data }}</h1>
    <h2>{{ title }}</h2>
    <p>{{ description }}</p>
  </article>
</template>

<style scoped>
.card {
  width: 350px;

  display: flex;
  padding: 50px 28px;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  border-radius: 20px;
  background: var(--NeutrosClarosBranco);
  box-shadow: 0px 8px 12px 0px rgb(0 0 0 / 9%);
  border: none;

  text-align: center;
  font-style: normal;
}

.card h1 {
  font-size: 80px;
  font-weight: 600;
  line-height: 91px;

  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin: 0;
}

.card h2 {
  font-size: 26px;
  font-weight: 600;
  line-height: 36px;
}

.card p {
  font-size: 14px;
  font-weight: 500;
  line-height: 21px;

  color: var(--AzulArdosia);
}

.purple {
  background-image: var(--GradienteRoxo);
}

.green {
  background-image: var(--GradientVerde);
}

.red {
  background-image: var(--GradientVermelho);
}

@media (max-width:1190px) {
  .card h1 {
    font-size: 80px;
    font-style: normal;
    font-weight: 600;
    line-height: 91px;
  }

  .card h2 {
    font-size: 20px;
    font-style: normal;
    font-weight: 600;
    line-height: 30px;
  }

  .card p {
    font-size: 12px;
    font-style: normal;
    font-weight: 500;
    line-height: 18px
  }
}
</style>