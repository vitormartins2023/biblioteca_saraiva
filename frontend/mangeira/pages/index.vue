<script setup lang ='ts'>
import { FORMATO, STATUS, type Livros } from '../models/livros';
import { onMounted } from 'vue';
import { getLivros } from "../services/livros";

getLivros().then
import { type Ref, ref } from 'vue';

const livros: Ref<Array<Livros>> = ref([]);
// ------------ TRAVEI NESSA PARTE---------------------------------------------------------------------------------------*************------------------------------------------
// Tentei importar o arquivo livros.ls dentro do services onde está fazendo o GET e ele nao reconhece, tentei importar tambem Livros da pasta models e ele tambem não reconhece
// pedi ajuda para os colegas de classe e nao consegui ter sucesso, com o tempo chegando ao fim estou enviado dessa forma.
// ----------------------------------------------------------------------------------------------------------------------*************------------------------------------------


//Se necessario autenticação só ativar
// definePageMeta({ 
//     middleware:'auth'
// });

// const LivroTeste: Livros = {
//     id: 1,
//     titulo:'livro teste',
//     descricao: 'Descricao do livro teste para testes para fazer um teste',
//     N_paginas: 10,
//     formato: FORMATO.E,
//     status: STATUS.A,
//     n_edicao: 2,
//     autor_FK:{
//         id:1,
//         nome:'Vitor',
//         biografia:'Bibliografia de vida',
//         foto:['https://img.freepik.com/fotos-gratis/representacao-da-experiencia-do-utilizador-e-design-da-interface_23-2150169847.jpg?size=626&ext=jpg'],
//         CustomUserFK:{
//             id: 1,
//             email: 'admin@admin.com',
//             telefone: '19983159285',
//             endereco: 'asdsadaadsdsa',
//             cpf:'asdsad',
//         },
//         nascimento: '02/01/2000',

//     },
//     dataPub: "01/01/2022",
//     valor_livro: 30.05,
//     estrela: 5,
//     estoque: 50,
//     categoria_FK:{
//         id:1,
//         nome: 'terror'
//     },
//     capa:["https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSDI5RpZVASIrgU9dTCdk2AtS_1wsZETXVHV9eNZls-IrbgpmBJwanavNSLX_7k3r_DC_fOpJXfby19bHIKEIMZ8IcBVS1gHXaSDBjKgUkG&usqp=CAc"

//     ]
// }

const atualizarProdutos = () => {
    getLivros().then(livrosEncontrados=>{
        console.log("Livros encontrados:", livrosEncontrados);
        livros.value = livrosEncontrados ?? []; // "??" quando aquele elemento pode exisitir ou nao
    });

};

atualizarProdutos();
</script>
<template >
    <main class="home-container flex felx-column align-items-center justify-content-center">
        <div class="livros-container grid align-items-center justify-content-center">
            <div v-for="(livro,index) in livros" :key="index" >
                <LivroItem :key="index" class="col-3" :livro="livro"/>

            </div>
    </div>
    <div class ="chat grid align-items-top justify-content-top">
    <iframe 
    allow="microphone;"
    width="350"
    height="430"
    src="https://console.dialogflow.com/api-client/demo/embedded/2ca2f691-76df-4530-b7e2-ec9ee68a134a">
</iframe>
    </div>
    </main>
    

</template>

<style scoped lang = "scss">

.home-container{
    margin:0;
    width: 100vw;
    min-height: calc(100vh - var(--altura-header));
    //background-image: url('background2.jpg');
    background-color: rgb(31, 31, 41);
    background-repeat: repeat;
    background-size: cover;
    

}
</style>