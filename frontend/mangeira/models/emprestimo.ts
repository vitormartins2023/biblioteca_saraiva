import type { Livros } from "./livros";
import type { Usuario } from "./usuario";

export type Emprestimos = {
    livro: Livros
    customUserFK : Usuario;
    valor_total: number;
    data_pegou: string;
    data_prevista: string;
    data_entrega: string;
}

export type Loanbody = {
    customUserFK: number;
    livro: Array<number>;
    valor_total: number;
}