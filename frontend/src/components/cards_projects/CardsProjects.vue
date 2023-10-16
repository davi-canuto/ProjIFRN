<script setup>
import ExploreCard from '../../components/cards/ExploreCard.vue';
</script>


<template>
    <section class="default-padding CardsProjects">
        <h1 class="">Explore nossa coleção de projetos</h1>

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

<style scoped>
.CardsProjects {
    margin: 117px 0px;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 80px;
}

.CardsProjects h1 {
    font-size: 44px;
    font-weight: 700;
    line-height: 66px;
}

.cards {
    display: flex;
    justify-content: space-between;
    gap: 5%;
    width: 100%;
}



@media (max-width:1190px) {
    .cards {
        overflow-x: scroll;
        width: 100%;
        display: inline-grid;
        justify-content: start;
        grid-auto-flow: column;
        padding: 1em;
    }

    .cards::-webkit-scrollbar {
        width: 0px;
    }

    .CardsProjects h1 {
        line-height: 52px;
    }


}
</style>