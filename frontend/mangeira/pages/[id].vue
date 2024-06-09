<script setup lang="ts">
import { type Ref, ref } from "vue";
import { type Livros } from "../models/livros";
import { getLivrosById } from "../services/livros";
const route = useRoute();

const produto: Ref<Livros|null> = ref(null);
    
const atualizarProduto = () => {
  if(route.params.id){
    getLivrosById(route.params.id as string).then((produtoEncontrado) => {
      console.log("produto encontrado: ", produtoEncontrado);
      produto.value = produtoEncontrado ?? null;
    });
  }
};

atualizarProduto();
</script>

<template> 
    <div><br>
    <section class=" cartao flex flex-column align-items-center justify-content-center"
    v-if = "produto">
            <div class="livro-imagem">
                <img :src="produto.capa">
            </div>
            <div>
                <h4>{{ produto.titulo }}</h4>
                <h2>{{ produto.autor_FK.nome }}</h2>
            </div>
            <div class = "flex flex-row align-content-between justify-content-between ">
            <span>R${{ produto.valor_livro }} - </span>
            <div class= "ml-2">
                <label>Qtd. Disponível</label>
                <span>{{ produto.estoque }}</span>
            </div>    
        </div>
        <div class ="botao-add">
        <Button :disabled="!produto.estoque" class="botao-add" 
        :label="produto.estoque? 'Adicionar' : 'Não disponível'" />
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