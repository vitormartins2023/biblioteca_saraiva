//import defineStore
import { defineStore } from "pinia";
import type { Livros } from "~/models/livros"

export type CarrinhoItem = {
    livro: Livros;
    quantidade: number;
}

export type Carrinho ={
    livro:Array<CarrinhoItem>;
}
export const carrinho = defineStore('carrinhoStore', {
    state: (): Carrinho=> ({
      livro: [] //Pinia vai criar uma variavel que vai ser compartilhada em varias telas
    }), 
    actions: {
      adicionarNoCarrinho(novoLivro: Livros){
        const livroJaExiste = this.getLivroDoCarrinho(novoLivro);
        if(livroJaExiste){
            livroJaExiste.quantidade += 1; //ta pegando o que existe e adicionando mais e guardando no mesmo lugar
            this.livro = [ // o novo carrinho vai ser o carrinho que ja existia menos o que ta igual + o novo com a quantidade nova
                // ... "tres pontinhos" faz uma copoia de um conjunto no JavaScript Vai copiar tudo o que tava e vai pegar o que ja existe e adiconar
                ...this.livro.filter(item=>item.livro.id !!= livroJaExiste.livro.id),
                livroJaExiste
            ];
        }
        //produto nao está no carrinho ainda
        else{ //push coloca mais 1 item em uma array
            this.livro.push({
                quantidade: 1,
                livro: novoLivro
            });
        }
      },
      removerDoCarrinho(carrinhoItem: CarrinhoItem){
        const posicaoNoCarrinho = this.getCarrinhoDoCarrinhoIndex(carrinhoItem.livro);
        //remove o item inteiro do carrinho
        this.livro.splice(posicaoNoCarrinho,1);
        if (carrinhoItem.quantidade){ // só att a nova qnt do item no carrinho
            this.livro = [ 
                // ele ja nao ta mais faço a copia "..." adiciono o novo item com a nova qnt
                ...this.livro,
                carrinhoItem
            ];
        }
        
      },
      esvaziarCarrinho(){
        this.livro = [];
      }
    },
    getters:{
        estaNoCarrinho: (carrinho:Carrinho) => (LivroParaEncontrar: Livros): boolean =>{
            return carrinho.livro.findIndex(item=>item.livro.id === LivroParaEncontrar.id) !== -1;
        },
        getLivroDoCarrinho: (carrinho:Carrinho) => (livroParaEcontrar: Livros) => { // para sabermos quanto e se ja foi adicionado
            return carrinho.livro.find(item=>item.livro.id === livroParaEcontrar.id);// para encontramos algo no typescript usanod find retorna o item
        },
        getCarrinhoDoCarrinhoIndex: (carrinho:Carrinho) => (livroParaEcontrar: Livros) => { // para sabermos quanto e se ja foi adicionado
            return carrinho.livro.findIndex(item=>item.livro.id === livroParaEcontrar.id);// para encontramos algo no typescript usanod find retorna a posição
        },
        getCarrinho: (carrinho: Carrinho) =>(): Array<CarrinhoItem>=>
        {
            return carrinho.livro;
        },

        getValorTotalDoCarrinho: (carrinho: Carrinho) => () : number => {
            let soma = 0;
            carrinho.livro.forEach(item=>{
                soma += (item.livro.valor_livro * item.quantidade)
            })
            return soma;
        }
    }
    
  })
  //actions seriam as ações de adicionar livro no carrinho