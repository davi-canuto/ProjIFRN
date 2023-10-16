<script setup>
import Search from '../search/Search.vue';

defineProps({})
</script>

<template>
    <header class="default-padding">
        <div class="navbar_left">
            <a href="#">
                <img src="../../assets/imgs/logotipo.svg" alt="projIFRN">
            </a>

            <Search class="searchbar" />
        </div>

        <ul class="navbar_right">
            <a href="#">
                <li class="navbar_link">
                    Explorar projetos
                </li>
            </a>

            <a href="#">
                <li class="navbar_link">
                    Entrar
                </li>
            </a>
        </ul>

        <img class="menu_btn" src="../../assets/icons/menu.svg">
    </header>
</template>



<style scoped>
a {
    text-decoration: none;
    color: initial;
}

header {
    display: flex;
    align-items: center;
    gap: 20%;
}

.navbar_left {
    display: flex;
    gap: 97px;
    align-items: center;
    width: 100%;
    height: 3.4em;
}

.navbar_right {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 32px;
}

ul {
    text-decoration: none;
    padding: 0;
    margin: 0;
    list-style: none;
}

li {
    width: max-content;
}

.menu_btn {
    display: none;
}

.navbar_link{
    font-weight: 700;
}

@media (max-width:1475px) {
    .bar_left {
        display: flex;
        gap: 65px;
    }
}

@media (max-width:1150px) {
    header {
        display: flex;
        align-items: center;
        gap: 10%;
    }
}

@media (max-width:900px) {
    header {
        display: flex;
        align-items: center;
        gap: 5%;
    }

    .navbar_right {
        display: none;
    }

    .searchbar {
        display: none;
    }

    .menu_btn {
        display: flex;
    }

}
</style>