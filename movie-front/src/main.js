import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import InfiniteLoading from 'v3-infinite-loading'
import "v3-infinite-loading/lib/style.css";


import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()

app.component("infinite-loading", InfiniteLoading)
pinia.use(piniaPluginPersistedstate)
app.use(pinia)
app.use(router)

app.mount('#app')
