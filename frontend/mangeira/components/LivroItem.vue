<script setup lang = "ts">
import { type Livros } from '../models/livros';
import { carrinho } from "../stores/carrinho";
import { computed } from 'vue';

const { adicionarNoCarrinho, getCarrinho, estaNoCarrinho } = carrinho();

const emit = defineEmits(['eventoAdicionado']); 

type propType ={
    livro: Livros;
}
const props = defineProps<propType>();
    const adicionarItem = () => {
    adicionarNoCarrinho(props.livro);
    emit('eventoAdicionado');
    console.log("CARRINHO ATUAL: ", getCarrinho());
}
const produtoNoCarrinho = computed(()=>{
  return estaNoCarrinho(props.livro);   
});
const detalheProduto = ()=>{
    const idProduto = props.livro.id;
    navigateTo(`/${idProduto}`);
}
</script>
<template> 
    <div><br>
    <section class=" cartao flex flex-column align-items-center justify-content-center"
    v-if = "props.livro">
            <div class="livro-imagem" @click="detalheProduto">
                <img :src="props.livro.capa"
                >
            </div>
            <div>
                <h4>{{ props.livro.titulo }}</h4>
            </div>
            <div class = "flex flex-row align-content-between justify-content-between ">
            <span>R${{ props.livro.valor_livro }} - </span>
            <div class= "ml-2">
                <label>Qtd. Disponível</label>
                <span>{{ props.livro.estoque }}</span>
            </div>    
        </div>
        <div class ="botao-add">
        <Button :disabled="!props.livro.estoque" @click="adicionarItem" class="botao-add" 
        :label="props.livro.estoque? 'Adicionar' : 'Não disponível'" />
        </div>
    
    </section>
    
</div>

</template>

<style scoped lang="scss">
    .cartao{
        width: 300px;
        max-width: 400px;
        height: 400px;
        max-height: 400px;
        background-color: white;
        border-radius: 1.5rem;
        margin: 1.5rem;
        cursor: pointer;

        
    &:hover{
        transform: scale (1.1);
        transition: 2s;
    }
        
    .livro-imagem{
        display:flex;
        align-items: center ;
        justify-content: center ;
        max-width: 300px;
        max-height: 200px;
        img{
        
        width: 87%;
        height: 100%;
        }
    } 
    .botao-add{
        display:flex;
        align-items: center ;
        justify-content: center ;
        width: 80%;
        height: 2rem;
        margin: 0.5rem;
    }


    }
</style>