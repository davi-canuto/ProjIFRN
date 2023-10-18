<script setup>
import HeaderBar from './components/header/HeaderBar.vue';
import Footer from './components/footer/Footer.vue';

</script>

<template>
  <HeaderBar />

  <router-view></router-view>
  <Footer></Footer>
</template>

<style>
:root {
  --AzulAco: #777E90;
  --AzulArdosia: #4A5568;
  --AzulEletrico: #408CFF;
  --AzulMarinhoEscuro: #131740;
  --BrancoFosco: #F5F7FA;
  --CinzaAzulado: #93989A;
  --GradientVerde: linear-gradient(93deg, #2AF598 -29.31%, #08AEEA 106.47%);
  --GradientVermelho: linear-gradient(93deg, #FF512F 3.55%, #DD2476 97.46%);
  --GradienteRoxo: linear-gradient(93deg, #FE6AB7 3.55%, #9B4AEB 47.23%, #3931F9 97.46%);
  --NeutrosClarosBranco: #FFFFFF;
  --VerdeEsmeralda: #00BF63;
}

body{
  color: var(--AzulMarinhoEscuro) !important;
  background: var(--BrancoFosco) !important;
}

.default-padding {
  padding: 40px 245px;
}

@media (max-width:1475px) {
  .default-padding {
    padding: 40px 122px;
  }
}

@media (max-width:1150px) {
  .default-padding {
    padding: 40px 61.25px;
  }
}

@media (max-width:750px) {
  .default-padding {
    padding: 40px 19px;
  }

}
</style>


