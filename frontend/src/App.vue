<script setup>
import ExploreCard from './components/cards/ExploreCard.vue';

</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03"
          aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <a class="navbar-brand" href="#">
          <img src="./assets/logotipo.svg">
        </a>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">

          <form class="navbar-nav me-auto mb-2 mb-lg-0" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
          <ul class="d-flex navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>

  <section>
    <h1 class="title-section"> Explore nossa coleção de projetos </h1>
    <div class="cards">
      <ExploreCard :data=22 title="Em Desenvolvimento"
        description="Testemunhe a evolução dos nossos projetos promissores em pleno desenvolvimento."
        title_gradient="purple" />

      <ExploreCard :data=35 title="Projetos Finalizados"
        description="Explore nossa galeria de projetos finalizados, resultados brilhantes e conquistas concluídas."
        title_gradient="green" />

      <ExploreCard :data=10 title="Projetos em Espera"
        description="Explore nossos projetos em espera, prontos para serem retomados e levados adiante."
        title_gradient="red" />
    </div>

  </section>
</template>

<style>
/* section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.cards {
  width: 80%;
  display: flex;
  justify-content: space-between;
}

.title-section {
  color: #131740;
  font-size: 44px;
  font-weight: 700;
  line-height: 66px;
  text-align: center;
  margin-bottom: 4rem;
} */
</style>


