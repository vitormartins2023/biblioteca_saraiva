<script setup lang = "ts">
import { type Livros } from '~/models/livros';
type propType ={
    livro: Livros;
}
const props = defineProps<propType>();
</script>
<template><br>
    
    <section class=" cartao flex flex-column align-items-center justify-content-center">
        <div class="livro-imagem">
            <img :src="props.livro.capa[0]">
        </div>
        <div>
            <h4>{{ props.livro.titulo }}</h4>
        </div>
        <div>
            <span>R${{ props.livro.valor_livro }}</span>
        </div>
        </section>
    
</template>
<style scoped lang="scss">
    .cartao{
        width: 300px;
        max-width: 300px;
        height: 350px;
        max-height: 350px;
        background-color: white;
        border-radius: 1.5rem;
        margin: 1.5rem;
        
    .livro-imagem img{
        width: 100%;
        height: 100%;
        }
    }
</style>