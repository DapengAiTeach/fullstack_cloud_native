import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './styles/global.css'
import 'element-plus/dist/index.css'
import router from './router/index.js'
import App from './App.vue'
import { useUserStore } from './store/user_store.js'

const app = createApp(App)

// 使用 Pinia
const pinia = createPinia()
app.use(pinia)

// 初始化用户数据（从 localStorage 恢复）
const userStore = useUserStore()
userStore.loadFromStorage()

app.use(router)
app.mount('#app')
