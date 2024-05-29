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

])
</script>
<template>
    <header>
        <div class ="flex align-items-center justify-content-center">
            <Menubar :model="ItensMenu" />
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