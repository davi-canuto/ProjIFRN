<script setup>
import Search from '../search/Search.vue';

defineProps({})
</script>

<template>
    <header>
        <div class="bar_left">
            <a href="#">
                <img src="../../assets/imgs/logotipo.svg" alt="projIFRN">
            </a>

            <Search />
        </div>

        <div class="bar_right">
            <ul>
                <li>
                    Explorar projetos
                </li>
                <li>
                    Explorar projetos
                </li>
            </ul>
        </div>
    </header>
</template>



<style scoped>
header {
    display: flex;
    align-items: center;
    padding: 40px 245px;
}



.bar_left {
    display: flex;
    gap: 97px;
    align-items: center;
    width: 100%;
}




@media (max-width:1475px) {
    header {
        padding: 40px 122px;
    }

    .bar_left {
        display: flex;
        gap: 97px;
    }
}

@media (max-width:1150px) {
    header {
        padding: 40px 61.25px;
    }
}

@media (max-width:750px) {
    header {
        padding: 40px 19px;
    }

}
</style>