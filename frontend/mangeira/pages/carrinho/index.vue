<script setup lang="ts">
import { computed, type Ref, ref } from "vue";
import { carrinho, type CarrinhoItem } from "../../stores/carrinho";
const { getCarrinho, removerDoCarrinho, getValorTotalDoCarrinho, esvaziarCarrinho } = carrinho();
import { salvarVenda, salvarVendaProdutos } from "../../services/emprestimo";
import { type Emprestimos, type Loanbody } from "../../models/emprestimo";
import { type Usuario } from "../../models/usuario";
import type { Livros } from "../../models/livros";
const { data } = useAuth();


definePageMeta({
    middleware: "auth",
});

const usuarioLogado = computed<any>(() => {
    if (data.value) {
        return data.value.results[0] ? data.value.results[0] as Usuario : null;
    }
    return null;
});

//pegando os itens que estão no carrinho e salvando
//na variavel
const itensNoCarrinho = computed<Array<CarrinhoItem>>(() => getCarrinho());
const valorTotal = computed(() => getValorTotalDoCarrinho());

const carregando = ref(false);
const salvo: Ref<boolean | null> = ref(null);

console.log("itens No carrinho.....", getCarrinho());

const deletarDoCarrinho = (itemParaRemover: CarrinhoItem) => {
    removerDoCarrinho({
        livro: itemParaRemover.livro,
        quantidade: 0
    });
}

const salvarPedido = () => {
    if (getCarrinho().length) {
        carregando.value = true;
        console.log("data", data.value)
        let meusLivros: Array<number> = [];
        getCarrinho().forEach(item => {
            meusLivros.push(
                item.livro.id
            );
        });

        let payload:Loanbody = {
            livro: meusLivros ?? [0],
            customUserFK: usuarioLogado.value?.id ?? 0,
            valor_total: valorTotal.value
        }
        console.log('payload: ', payload)
        salvarVendaProdutos(payload).then(resposta => {
            console.log("ITENS DE VENDA SALVOS!", resposta);
            setTimeout(() => {
                salvo.value = true;
                esvaziarCarrinho();
            }, 3000);
            }).catch(error => {
                salvo.value = false;
                console.error("Erro ao salvar venda! ", error);
            })
            .then(() => {
                console.log("SALVO STATUS", salvo)
                setTimeout(() => {
                    carregando.value = false;
                    salvo.value = null;
                }, 3000);
            });
    console.log(payload);
    }
}



</script>

<template>
    <main class="carrinho-container flex flex-column align-items-center">
        <h2 class="mt-4 mb-4">🛒 Seu carrinho de compras</h2>
        <div class="card flex justify-content-center" v-if="carregando">
            <ProgressSpinner />
        </div>
        <table v-if="!carregando">
            <thead>
                <tr class="text-center">
                    <td>Item</td>
                    <td>Produto</td>
                    <td>Descrição</td>
                    <td>Preço Unitário</td>
                    <td>Ações</td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(itemCarrinho, index) in itensNoCarrinho" :key="index" class="text-center">
                    <td>{{ index + 1 }}</td>
                    <td><img class="fotoProduto" :src="itemCarrinho.livro.capa" alt="foto produto" /></td>
                    <td>{{ itemCarrinho.livro.titulo }}</td>
                    <td>R$ {{ itemCarrinho.livro.valor_livro }}</td>
                    <td>
                        <Button @click="deletarDoCarrinho(itemCarrinho)" label=""><i class="pi pi-trash"></i></Button>
                    </td>
                </tr>
            </tbody>
            <tfoot>
                <tr class="text-center">
                    <th></th>
                    <th></th>
                    <th>Valor Total:</th>
                    <th>R${{ valorTotal }}</th>
                </tr>
            </tfoot>
        </table>
        <Button :disabled="salvo !== null" v-if="!carregando" @click="salvarPedido" class="mt-2 botao-pedido bg-primary"
            label="Fechar pedido" />
        <Message v-if="salvo === true" severity="success">
            <p>Pedido realizado com sucesso!</p>
            <p>Consulte seus itens em <NuxtLink to="/Emprestimo">Meus Pedidos</NuxtLink>
            </p>
        </Message>
        <Message v-if="salvo === false" severity="error">
            <p>Não foi possível salvar esta venda! 😥</p>
        </Message>


    </main>
</template>

<style scoped lang="scss">
$largura-tabela: 90vw;

.carrinho-container {
    margin: 0;
    width: 100vw;
    min-height: calc(100vh - 80px);
    background-color: red;
    background-image: url("background1.jpg");
    background-repeat: repeat;
    background-size: cover;
}

table {
    width: $largura-tabela;
    background-color: white;
    border-radius: 1rem;
}

thead {
    font-weight: bold;

    tr {
        border-bottom: 2px solid black
    }
}

td {
    padding: 1rem;
}

.fotoProduto {
    width: 50px;
    height: 50px;
}

Button {
    background-color: white;
    color: rgb(114, 15, 15);
    border: none;
}

.valor-total {
    font-weight: bold;
    width: 900px
}

.botao-pedido {
    width: $largura-tabela;
    height: 30px;

    &:hover {
        transform: scale(1.05);
        transition: 2s;
    }
}
</style>