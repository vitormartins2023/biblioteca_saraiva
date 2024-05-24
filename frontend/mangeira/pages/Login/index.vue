<script setup lang ='ts'> 
import {reactive} from 'vue';
    const credenciais = reactive({
        email:'',
        password:''
    });
    const fazerLogin =() => {
        console.log("login: ", credenciais)
    }
</script>

<template>
    <main class="login-main flex-initial flex align-items-center justify-content-center ">
        <section class ="login-container flex flex-column flex align-items-center justify-content-center ">
            <h4 class ="row-login">Seraiva</h4>
            <div class="row-login">
                <FloatLabel>
                    <InputText v-model ="credenciais.email" id="email-input" class ="input-text"/>
                    <label for="email-input">Email</label>
                </FloatLabel>
            </div>
            <div class ="row-login">
                <FloatLabel>
                    <InputText v-model ="credenciais.password" type = "password" id="passoword-input" class ="input-text"/>
                    <label for="passoword-input">Senha</label>
                </FloatLabel>
            </div>
            <div class ="row-login">
                <Button @click="fazerLogin" label="Entrar" id="login-button"></Button>
            </div>
        </section>

    </main>
</template>



<style scoped lang = "scss">
    .login-main{
        width: 100vw;
        height: 100vh;
        background-image: url('background1.jpg');
        background-repeat: repeat;
        background-size: contain;

        .login-container{
            width: 30vw;
            height: 70vh;
            background-color:  rgb(150, 146, 139);

        .row-login{
            
            margin: 1rem 0 1rem 0;
            .input-text{
                height: 2.5rem;
                width: 250px;
            }
            #login-button{
                
                height: 30px;
                width: 250px;
            }
            

        }
    }
}

</style>