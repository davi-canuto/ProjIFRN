<script setup>
defineProps({})
</script>

<template>
    <section class="hero-section default-padding">
        <h1>Compartilhando <br> Inovação Acadêmica</h1>
        <p>Compartilhe e explore os projetos <span class="text-responsive">de desenvolvimento de software <br>
            </span> implementados
            pela comunidade acadêmica do IFRN Campus - CNAT</p>

    </section>
</template>

<style scoped>
.hero-section {
    height: 718px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.hero-section h1 {
    font-size: 80px;
    font-weight: 600;
    line-height: 91px;
    text-align: center;
}

.hero-section p {
    font-size: 24px;
    font-weight: 500;
    line-height: 36px;
    text-align: center;
}



@media (max-width:900px) {
    .hero-section h1 {
        font-size: 44px;
        font-style: normal;
        font-weight: 700;
        line-height: 52px;
    }

    .hero-section p {
        font-size: 16px;
        font-weight: 400;
        line-height: 24px;
        text-align: center;
    }

    .hero-section .text-responsive {
        display: none;
    }
}
</style>