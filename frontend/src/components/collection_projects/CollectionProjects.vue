<script setup>
import ProjectCard from '../cards/ProjectCard.vue';
import { ref, onMounted } from 'vue';
import projectsService from "../../services/projectsServices";
defineProps({
    title: String,
})

const projects = ref([]);

const fetchProjects = async () => {
  try {
    const response = await projectsService.getProjects();
    projects.value = response;

} catch (error) {
    console.error('Erro ao buscar dados da API:', error);
  }
};
const projectsRefs = ref([])

onMounted(() => {
  fetchProjects();
});
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
        
            <ProjectCard  v-for="project in projects" ref="projectsRefs" :title="project.title" :description="project.description" :step="project.step"
                leader="André Silva"  />

           
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
    overflow-x: auto;
    width: 100%;
    display: inline-grid;
    justify-content: start;
    grid-auto-flow: column;
    padding: 1em;
    gap: 2em;
}

.content::-webkit-scrollbar {
    width: 5px;
    height: 8px;
}

.content::-webkit-scrollbar-thumb {
    background-color: #cccccc;
    border-radius: 4em;
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

@media (max-width:990px) {
    .section {
        gap: 47px;
    }

    .content {
        display: flex;
        flex-direction: column;
    }
}
</style>