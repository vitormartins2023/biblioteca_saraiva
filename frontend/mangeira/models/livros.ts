import type { Usuario } from "./usuario";
export enum FORMATO{
    "E" = "Ebook",
    "F" = "Fisico",
}

export enum STATUS{
    "P" = "Pendente",
    "A" = "Aprovado",
    "R" = "Recusado",
}

export type Categoria={
    id:number;
    nome: string;
}

export type Autor={
    id: number;
    nome: string;
    biografia: string;
    foto: Array<string>;
    CustomUserFK: Usuario;
    nascimento: string;

} 

export type Livros={
    id:number;
    titulo: string;
    descricao: string;
    N_paginas: number;
    formato: FORMATO;
    status: STATUS;
    n_edicao: number;
    autor_FK: Autor;
    categoria_FK: Categoria;
    dataPub: string;
    valor_livro: number;
    capa: string;
    estrela: number;
    estoque: number;

}