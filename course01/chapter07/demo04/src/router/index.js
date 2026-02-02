import { createRouter, createWebHistory } from 'vue-router'

// 路由列表
const routes = [
    {
        path: '/',
        component: () => import('@/layout/layout.vue'),
        redirect: '/blog',
        children: [
            {
                path: '/blog',
                component: () => import('@/page/blog.vue'),
            }
        ]
    },
]
// 路由器
const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router