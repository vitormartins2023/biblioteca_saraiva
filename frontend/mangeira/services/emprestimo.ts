import { BACKEND_URL } from "~/models/app";
import type { Emprestimos, Loanbody } from "~/models/emprestimo";

export const salvarVenda = async (venda: Emprestimos): Promise<Emprestimos | null> => {
  const {error,data} = await useFetch<Emprestimos>(`${BACKEND_URL}/Emprestimo/`, {
    method: 'POST',
    body: venda
  })

  if(error.value){
    console.log("error useFetch", error.value);
    return Promise.reject(null);
  }
  
  return Promise.resolve(data.value);

    /*.then(resposta => {
      console.log("success response")
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.reject(null);
    })*/
};


export const salvarVendaProdutos = (emprestimo: Loanbody): Promise<Emprestimos | null> => {
  return useFetch<Emprestimos>(`${BACKEND_URL}/Emprestimo/`, {
    method: 'POST',
    body: emprestimo
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.reject(null);
    })
};