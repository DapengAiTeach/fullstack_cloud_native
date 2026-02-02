import { createRouter, createWebHistory } from 'vue-router'

// 路由列表（layout 为顶层布局，子路由渲染到 layout 的 <router-view />）
const routes = [
    {
        path: '/',
        component: () => import('@/layout/layout.vue'),
        children: [
            { path: '', component: () => import('@/page/home.vue') },
            { path: 'blog', component: () => import('@/page/blog.vue') },
        ],
    },
]

// 路由器
const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router