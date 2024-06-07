import { BACKEND_URL } from "~/models/app"
import type { Livros } from "~/models/livros"
import type { Pagination } from "~/models/paginations";

export const getLivros = (numeroPagina: number = 0): Promise<Pagination<Livros>|null>=> {
    return useFetch<Pagination<Livros>>(`${BACKEND_URL}/livros?page=${numeroPagina}`)
        .then(response=> Promise.resolve(response.data.value))
        .catch(error=>{
            console.error(error);
            Promise.resolve(null);
    }) as Promise<Pagination<Livros>|null>;
};
