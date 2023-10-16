<script setup>
defineProps({})
</script>

<template>
    <section class="logos default-padding">
        <img src="../../assets/imgs/diatinf-logo.svg" alt="projIFRN">
        <img src="../../assets/imgs/ifrn-logo.svg" alt="projIFRN">
        <img src="../../assets/imgs/tads-logo.svg" alt="projIFRN">
    </section>
</template>



<style scoped>
.logos {
    border-width: 2px 0;
    border-style: solid;
    border-image: linear-gradient(to right, rgba(192, 204, 218, 0.1), rgba(192, 204, 218, 0.6), rgba(192, 204, 218, 0.1)) 1;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 155px;
}


@media (max-width:900px) {
    .logos {
        gap: 1em;
    }

    .logos img{
        width: 81px;
    }
}
</style>