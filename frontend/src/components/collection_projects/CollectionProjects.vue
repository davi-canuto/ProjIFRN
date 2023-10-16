<script setup>
import ProjectCard from '../cards/ProjectCard.vue';

defineProps({
    title: String
})

</script>

<template>
    <section class="default-padding">
        <div class="header">
            <h1>{{ title }}</h1>
            <a href="#">
                <p>Ver Todos</p>
            </a>
        </div>

        <div class="content">
            <ProjectCard title="StockWeb+" description="Sistema de Gerenciamento de Estoque Online" step="PDS web"
                leader="André Silva" startdate="04-2019" />

            <ProjectCard title="StockWeb+" description="Sistema de Gerenciamento de Estoque Online" step="PDS web"
                leader="André Silva" startdate="04-2019" />

            <ProjectCard title="StockWeb+" description="Sistema de Gerenciamento de Estoque Online" step="PDS web"
                leader="André Silva" startdate="04-2019" />
        </div>
    </section>
</template>

<style scoped>
section {
    display: flex;
    flex-direction: column;
    gap: 80px;
}

a {
    text-decoration: none;
    color: initial;
}

.header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-end;
}

.header h1 {
    font-size: 44px;
    font-weight: 700;
    line-height: 66px;
}

.header a p {
    font-size: 20px;
    font-style: normal;
    font-weight: 600;
    line-height: 30px;
    color: var(--VerdeEsmeralda);
}

.content {
    display: flex;
    justify-content: space-between;
}

@media (max-width:1190px) {
    .header {
        flex-direction: column;
        gap: 29px;
        align-items: flex-start;
    }

    .header h1 {
        line-height: 52px;
    }

    .header a p {
        border-radius: 38px;
        background: var(--Verde-Esmeralda, #00BF63);
        padding: 12px 20px;
        color: var(--NeutrosClarosBranco);

    }
}
</style>