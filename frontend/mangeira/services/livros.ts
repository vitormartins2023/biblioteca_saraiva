import { type Ref } from "vue";
import { BACKEND_URL } from "~/models/app"
import type { Livros } from "~/models/livros"
import type { Pagination } from "~/models/paginations";

export const getLivros = (numeroPagina: number = 0): Promise<Array<Livros>|null>=> {
    return useFetch<Array<Livros>>(`${BACKEND_URL}/livros?page=${numeroPagina}`)
        .then(response=> {
            return Promise.resolve(response.data.value);
        })
        .catch(error=>{
            console.log("error",error);
            return Promise.resolve(null);
    }) 
};

export const getLivrosById = (id:string): Promise<Livros|null>=> {
    return useFetch<Livros>(`${BACKEND_URL}/livros/${id}`)
        .then(response=> {
            return Promise.resolve(response.data.value);
        })
        .catch(error=>{
            console.log("error",error);
            return Promise.resolve(null);
    }) 
};