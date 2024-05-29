<script setup lang ='ts'>
import type { Livros } from '~/models/livros';
import { getLivros } from "~/services/livros";
getLivros().then

// ------------ TRAVEI NESSA PARTE---------------------------------------------------------------------------------------*************------------------------------------------
// Tentei importar o arquivo livros.ls dentro do services onde está fazendo o GET e ele nao reconhece, tentei importar tambem Livros da pasta models e ele tambem não reconhece
// pedi ajuda para os colegas de classe e nao consegui ter sucesso, com o tempo chegando ao fim estou enviado dessa forma.
// ----------------------------------------------------------------------------------------------------------------------*************------------------------------------------


//Se necessario autenticação só ativar
// definePageMeta({ 
//     middleware:'auth'
// });
</script>
<template>
    <main class="home-container">
        
    </main>
</template>
<style scoped lang = "scss">

.home-container{
    margin:0;
    width: 100vw;
    min-height: calc(100vh - var(--altura-header));
    background-image: url('background2.jpg');
    background-repeat: repeat;
    background-size: contain;
}
</style>