import { BACKEND_URL } from "~/models/app"
import type { Livros } from "~/models/livros"
import type { Pagination } from "~/models/paginations";

export const getLivros = (numeroPagina: number = 0): Promise<Pagination<Livros>|null>=> {
    let data: Pagination<Livros>|null = null;
    useFetch<Pagination<Livros>>(`${BACKEND_URL}/livros?page=${numeroPagina}`)
        .then(response=> {
            data = response.data.value;
        })
        .catch(error=>console.error(error));
    return Promise.resolve(data);
    };
