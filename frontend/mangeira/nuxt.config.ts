// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth',
    '@pinia/nuxt',
  ],
  primevue: {
    components:{
      include:['Button', 'Avatar','InputText','floatlabel','Menubar']
    }
  },
  // para fazer importações globais
  css:[
    'primeicons/primeicons.css',
    'primevue/resources/themes/aura-light-green/theme.css',
    'primeflex/primeflex.css',
    '~/assets/global.scss',
    
  ],
  auth: {
    baseURL: 'https://somativa-andre-2341-production.up.railway.app/api/auth',
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },
        signOut: { path: '/token/logout', method: 'post' },
        getSession: { path: '/users', method: 'get' },
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
      pages: { login: '/login' }, //altera quando for em outra pagina para logar
      sessionDataType: {
        results: 'Array'
      }
    }
  }
})
