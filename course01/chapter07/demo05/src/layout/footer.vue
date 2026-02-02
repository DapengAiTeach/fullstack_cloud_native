<script setup>
import { ref } from 'vue'

const email = ref('')
const subscribing = ref(false)

const subscribe = () => {
    if (!email.value || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email.value)) {
        alert('请输入有效的邮箱地址')
        return
    }
    subscribing.value = true
    // 模拟异步提交
    setTimeout(() => {
        subscribing.value = false
        alert('已订阅，感谢！')
        email.value = ''
    }, 800)
}
</script>

<template>
    <footer class="bg-gray-50 dark:bg-gray-900 text-gray-700 dark:text-gray-300 border-t border-gray-200 dark:border-gray-800">
        <div class="container-wrapper py-10">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
                <!-- 关于 / 品牌 -->
                <div class="space-y-4">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 bg-blue-600 rounded-md flex items-center justify-center text-white font-bold">B</div>
                        <div class="text-lg font-semibold">MyBlog</div>
                    </div>
                    <p class="text-sm text-gray-600 dark:text-gray-400">分享技术见解与实践经验，记录成长与思考。</p>
                    <div class="flex items-center space-x-3 mt-2">
                        <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">GitHub</a>
                        <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">微博</a>
                        <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">微信</a>
                    </div>
                </div>

                <!-- 快速导航 -->
                <div>
                    <h3 class="text-sm font-semibold mb-3">快速导航</h3>
                    <ul class="space-y-2 text-sm text-gray-600 dark:text-gray-400">
                        <li><router-link to="/">首页</router-link></li>
                        <li><router-link to="/blog">博客</router-link></li>
                        <li><router-link to="/categories">分类</router-link></li>
                        <li><router-link to="/about">关于</router-link></li>
                        <li><router-link to="/contact">联系</router-link></li>
                    </ul>
                </div>

                <!-- 推荐文章（占位） -->
                <div>
                    <h3 class="text-sm font-semibold mb-3">推荐阅读</h3>
                    <ul class="space-y-2 text-sm text-gray-600 dark:text-gray-400">
                        <li><a href="#">如何写出高质量的技术文章</a></li>
                        <li><a href="#">前端性能优化整理</a></li>
                        <li><a href="#">从零搭建个人博客</a></li>
                    </ul>
                </div>

                <!-- 订阅 -->
                <div>
                    <h3 class="text-sm font-semibold mb-3">订阅邮件</h3>
                    <p class="text-sm text-gray-600 dark:text-gray-400 mb-3">订阅最新文章与更新（不会滥发）</p>
                    <div class="flex items-center space-x-2">
                        <input v-model="email" type="email" placeholder="输入你的邮箱"
                                     class="flex-1 px-3 py-2 rounded-l-md bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 outline-none text-sm" />
                        <button @click="subscribe" :disabled="subscribing" class="px-4 py-2 bg-blue-600 text-white rounded-r-md text-sm hover:bg-blue-700 transition-colors">
                            {{ subscribing ? '订阅中...' : '订阅' }}
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <div class="container-wrapper">
                <hr class="mx-auto my-4 w-full max-w-xs border-t border-gray-300/60 dark:border-gray-700/60" />
            </div>

            <div class="container-wrapper py-4 flex flex-col md:flex-row items-center justify-between text-sm text-gray-500">
                <div>© {{ new Date().getFullYear() }} MyBlog. 保留所有权利。 | ICP 备案号：示例ICP备000000号</div>
                <div class="mt-3 md:mt-0">由 MyBlog 提供技术支持</div>
            </div>
        </div>
    </footer>
</template>