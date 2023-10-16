<script setup>
import ExploreCard from '../components/cards/ExploreCard.vue';

</script>

<template>
    <div >
        <section class="start-home">
            <h1  class="display-1 text-center"><strong>Compartilhando <br> Inovação Acadêmica </strong> </h1>
            <p class="text-center mb-5">Compartilhe e explore os projetos de desenvolvimento de software <br> implementados pela comunidade acadêmica do IFRN Campus - CNAT</p>

            <div class="logos mt-5 d-flex justify-content-center py-4 ">
                <img src="../assets/imgs/diatinf-logo.svg" alt="projIFRN">
                <img src="../assets/imgs/ifrn-logo.svg" alt="projIFRN">
                <img src="../assets/imgs/tads-logo.svg" alt="projIFRN">

            </div>
        </section>
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
    </div>   
</template>



<style scoped>

 section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.start-home{
    color: var(--AzulMarinhoEscuro);
    height: 90vh;
}
.start-home p{
    font-size: 1.5rem;
    font-weight: 600;
}

.logos{
    border-width: 2px 0;
    border-style: solid;
    border-image: linear-gradient(to right,rgba(192, 204, 218, 0.1), rgba(192, 204, 218, 0.6), rgba(192, 204, 218, 0.1)) 1;

    width: 100%;
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
} 
</style>