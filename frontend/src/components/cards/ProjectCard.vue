<script setup>
defineProps({
    title: String,
    description: String,
    step: String,
    leader: String,
    thumbnail: String
})

</script>

<template>
    <div class="project-div">
        <img class="wallpaper" src="../../assets/imgs/wallpaper.png">

        <div class="datas">
            <span class="step">{{ step }}</span>
            <div>
                <h1 class="title">{{ title }}</h1>
                <p class="description">{{ description }}</p>
            </div>
            <div class="data_user">
                <img src="../../assets/imgs/perfil.jpg" alt="#">

                <div class="names">
                    <h3>Prof. {{ leader }}</h3>
                    <p>Orientador</p>
                </div>
            </div>
        </div>
        <div class="footer">
            <div class="details">
                <!-- <h2>Desde {{ startdate }}</h2> -->
                <p>mais detalhes</p>
            </div>
            <img src="../../assets/icons/go.svg">
        </div>
    </div>
</template>

<style scoped>
.project-div {
    display: inline-flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 13px;

    border-radius: 6.83px;
    background: var(--NeutrosClarosBranco);
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
    width: 320px;
}

.project-div .wallpaper {
    width: 100%;
    height: 279px;
    object-fit: cover;
    border-radius: inherit;
}

.project-div .datas {
    display: flex;
    padding: 25px 23px 0px 23px;
    flex-direction: column;
    align-items: flex-start;
    gap: 13px;
    align-self: stretch;
}

.project-div .datas .step {
    border-radius: 5px;
    background: var(--AzulEletrico);
    color: var(--NeutrosClarosBranco);
    width: 57px;
    height: 20px;
    text-align: center;

    font-size: 12px;
    font-style: normal;
    font-weight: 500;
}

.project-div .datas .title {
    font-size: 16px;
    font-style: normal;
    font-weight: 700;
    line-height: 24px;
    margin: 0;
}

.project-div .datas .description {
    font-size: 12px;
    font-style: normal;
    font-weight: 500;
    line-height: 18px;
    margin: 0;
    color: var(--AzulArdosia);
}


.project-div .datas .data_user {
    display: flex;
    flex-direction: row;
    gap: 1em;
    align-items: center;
}

.project-div .datas .data_user img {
    width: 41px;
    height: 41px;
    border-radius: 50%;
}

.project-div .datas .data_user .names {
    display: flex;
    flex-direction: column;
}

.project-div .datas .data_user .names h3 {
    font-size: 12px;
    font-style: normal;
    font-weight: 600;
    line-height: 18px;
    margin: 0;
}

.project-div .datas .data_user .names p {
    font-size: 12px;
    font-style: normal;
    font-weight: 400;
    line-height: 18px;
    margin: 0;
}

.footer {
    width: 100%;
    padding: 13px 23px 13px 23px;
    border-top: 1px solid #DFDFDF;
    display: flex;
    justify-content: space-between;
}

.footer .details h2 {
    font-size: 12px;
    font-style: normal;
    font-weight: 700;
    line-height: 18px;
    margin: 0;
}

.footer .details p {
    font-size: 12px;
    font-style: normal;
    font-weight: 500;
    line-height: 18px;
    margin: 0;
    color: var(--VerdeEsmeralda);
}

@media (max-width:990px) {
    .wallpaper {
        display: none;
    }

    .project-div {
        width: 100%;
        box-shadow: 0px 4px 5px 0px rgba(0, 0, 0, 0.25);
    }
}
</style>