import { createRouter, createWebHistory } from 'vue-router'

// 路由列表（layout 为顶层布局，子路由渲染到 layout 的 <router-view />）
const routes = [
    {
        path: '/',
        component: () => import('@/layout/layout.vue'),
        children: [
            { path: '', component: () => import('@/page/home.vue') },
            { path: 'blog', component: () => import('@/page/blog.vue') },
            { path: 'categories', component: () => import('@/page/categories.vue') },
            { path: 'about', component: () => import('@/page/about.vue') },
            { path: 'contact', component: () => import('@/page/contact.vue') },
            { path: 'profile', component: () => import('@/page/profile.vue') },
            { path: 'favorites', component: () => import('@/page/favorites.vue') },
            { path: 'settings', component: () => import('@/page/settings.vue') },
        ],
    },
]

// 路由器
const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router