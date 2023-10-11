<script setup>
import ExploreCard from './components/cards/ExploreCard.vue';
import Search from './components/header/Search.vue';
</script>

<template>
  <Header>
    <a href="#">
      <img src="./assets/imgs/logotipo.svg" alt="projIFRN">
    </a>
    <Search />
  </Header>

  <!-- <section>
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

  </section> -->
</template>

<style>
:root{
  --AzulAco :#777E90;
  --AzulArdosia:#4A5568;
  --AzulEletrico: #408CFF;
  --AzulMarinhoEscuro:#131740;
  --BrancoFosco:#F5F7FA;
  --CinzaAzulado: #93989A;
  --GradientVerde:linear-gradient(93deg, #2AF598 -29.31%, #08AEEA 106.47%);
  --GradientVermelho: linear-gradient(93deg, #FF512F 3.55%, #DD2476 97.46%); ;
  --GradienteRoxo:linear-gradient(93deg, #FE6AB7 3.55%, #9B4AEB 47.23%, #3931F9 97.46%);
  --NeutrosClarosBranco:#FFFFFF;
  --VerdeEsmeralda:#00BF63;  
}

header {
  display: flex;
  align-items: center;
}

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


