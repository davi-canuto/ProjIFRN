<script setup>
defineProps({})
</script>

<template>
    <form class="form_search">
        <input class="search" type="text" name="" id="" placeholder="Pesquise  por projeto, membros, palavras-chave...">
        <img class="icon" src="../../assets/icons/search.svg" alt="52">
    </form>
</template>



<style scoped>
.form_search {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    width: 100%;
}

.search {
    border-radius: 20px;
    border: 1px solid rgba(0, 0, 0, 0.10);

    display: flex;
    width: 100%;
    height: 52px;
    padding: 15px 40px 15px 20px;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
    flex-shrink: 0;

    font-weight: 500;
    font-style: normal;
    line-height: normal;
    
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;

    background: var(--BrancoFosco);
    color: var(--CinzaAzulado);
}
.search:focus {
    outline: none;
    border: 1px solid rgba(0, 0, 0, 0.30);
}
.icon{
    margin-right: 16px;
    position: absolute;
}
</style>