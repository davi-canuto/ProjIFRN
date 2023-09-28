<script setup>
import ExploreCard from './components/cards/ExploreCard.vue';

</script>

<template>
  <section >
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
  section{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }  
  .cards{
    width: 80%;
    display: flex;
    justify-content: space-between;
  }
  .title-section{
    color: #131740;
    font-size: 44px;
    font-weight: 700;
    line-height: 66px; 
    text-align: center;
    margin-bottom: 4rem;
  }
</style>


