<script setup>

defineProps({})
</script>

<template>
    <footer class="default-padding">
        <div class="primary-footer d-flex justify-content-between">
            <div class="footer_left">
                <img class="mb-3" src="../../assets/imgs/logo-light.svg" alt="projIFRN">
                <p> <strong> INSTITUTO FEDERAL DO RIO GRANDE DO NORTE</strong> <br>
                CAMPUS NATAL - CENTRAL</p>
            </div>

            <div class="footer_right">
                <h1 class="footer_title mb-3"> Links Úteis</h1>
                <ul>
                    <li><a href="https://portal.ifrn.edu.br/" target="_blank"> Portal IFRN </a></li>
                    <li><a href="https://suap.ifrn.edu.br/" target="_blank"> SUAP </a></li>
                    <li><a href="https://diatinf.ifrn.edu.br/" target="_blank"> DIATINF </a></li>
                    <li><a href="#" target="_blank"> Projeto ProjIFRN </a></li>
                </ul>
            </div>
        </div>
        <div class="d-flex secondary-footer">
            <a href="#" target="_blank"> Termos de uso </a>
            <a href="#" target="_blank"> Política de Privacidade </a>
        </div>
    </footer>
</template>



<style scoped>
footer{
    background-color: var(--PretoProfundo);
    color: var(--AzulAco);
}
footer a{
    color: var(--AzulAco);
}
footer a:hover{
    color: var(--BrancoFosco);
    cursor: pointer;
}
footer{
    background-color: var(--PretoProfundo);
    color: var(--AzulAco);
}

footer ul li{
    margin-bottom: 15px;
}
.footer_left{
    color: var(--AzulAco);
}
.footer_right{
    text-align: right;
}
.footer_title{
    color: var(--BrancoFosco);
    font-size: 18px;
    font-weight: 600;
}
.secondary-footer{
    border-top-width: 1px;
    border-right-width: 0;
    border-bottom-width: 1px;
    border-left-width: 0;
    border-style: solid;
    border-color: rgba(119, 126, 144, .3);
    gap: 32px;
    
}

.secondary-footer a{
    margin: 35px 0;
}
@media (max-width:1475px) {

}

@media (max-width:1150px) {
   
}

@media (max-width:900px) {
    .primary-footer{
        flex-direction: column-reverse!important;
    }
    .footer_right{
        text-align: left;
        margin-bottom: 34px;
    }
    ul{
        padding: 0;
    }

}
</style>