<script setup lang ='ts'> 
import { ref } from 'vue';

const ItensMenu = ref([
    {
        label: 'Home',
        icon: 'pi pi-home'
    },
    
    {
        label: 'Meus pedidos',
        icon: 'pi pi-briefcase'
    },

    {
        label: 'Meus pedidos',
        icon: 'pi pi-users'
    },



])
</script>
<template>
    <header>
        <div class="flex align-items-center justify-content-center">
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-home mr-1"></i>
          <NuxtLink to="/">Livros</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-shopping-cart mr-1"></i>
          <NuxtLink to="/carrinho">Carrinho</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-users-cart mr-1"></i>
          <NuxtLink to="/login">Login</NuxtLink>
        </div>

    </div>
    </header>
</template>
<style scoped lang = "scss">
    header{
        width: 100vw;
        height: var(--altura-header);
        border-bottom: 1px solid black;
        .p-menubar{
            height:  50px;
            border: none;
            
            .p-menuitem{
                margin: 0 1rem 0 1rem;
            }
        }
    }

</style>