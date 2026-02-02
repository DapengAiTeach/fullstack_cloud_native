<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const articles = ref([
  {
    id: 1,
    title: '如何写出高质量的技术文章',
    excerpt: '从选题、结构、示例到发布后的维护，逐步讲解写作流程与注意事项。',
    tag: '写作',
    date: '2024-01-15',
    path: '/blog/1'
  },
  {
    id: 2,
    title: '前端性能优化整理',
    excerpt: '收集常见性能问题与对应优化策略，包含资源加载和渲染优化。',
    tag: '前端',
    date: '2024-01-10',
    path: '/blog/2'
  },
  {
    id: 3,
    title: '从零搭建个人博客',
    excerpt: '一步步搭建博客的技术选型、部署流程和持续集成实践。',
    tag: '运维',
    date: '2024-01-05',
    path: '/blog/3'
  },
  {
    id: 4,
    title: '现代 CSS 布局详解',
    excerpt: '比较 Flexbox、Grid 与新兴布局技巧，给出实战示例。',
    tag: '前端',
    date: '2024-01-02',
    path: '/blog/4'
  },
])

const openArticle = (path) => {
  router.push(path)
}
</script>

<template>
  <section class="container-wrapper py-12">
    <!-- 页面标题 -->
    <div class="text-center max-w-2xl mx-auto mb-10">
      <h1 class="text-3xl md:text-4xl font-extrabold">博客文章</h1>
      <p class="mt-2 text-gray-600 dark:text-gray-400">分享技术见解与实践经验</p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- 文章列表主区域（占 2 列） -->
      <div class="lg:col-span-2">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-6">
          <article v-for="item in articles" :key="item.id" class="bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-lg shadow-sm overflow-hidden">
            <div class="p-4">
              <div class="flex items-center justify-between">
                <span class="text-xs bg-blue-50 text-blue-600 px-2 py-1 rounded">{{ item.tag }}</span>
                <time class="text-xs text-gray-400">{{ item.date }}</time>
              </div>
              <h2 class="mt-3 text-lg font-semibold text-gray-900 dark:text-gray-100 hover:text-blue-600 cursor-pointer" @click="openArticle(item.path)">{{ item.title }}</h2>
              <p class="mt-2 text-sm text-gray-600 dark:text-gray-400">{{ item.excerpt }}</p>
            </div>
            <div class="p-4 pt-0">
              <button @click="openArticle(item.path)" class="text-sm text-blue-600 hover:underline">阅读更多 →</button>
            </div>
          </article>
        </div>

        <!-- 分页占位 -->
        <div class="mt-8 flex justify-center">
          <nav class="inline-flex items-center space-x-2 bg-white dark:bg-gray-800 px-4 py-2 rounded-md border border-gray-100 dark:border-gray-700">
            <button class="px-3 py-1 text-sm text-gray-600 dark:text-gray-300">上一页</button>
            <button class="px-3 py-1 text-sm bg-blue-600 text-white rounded">1</button>
            <button class="px-3 py-1 text-sm text-gray-600 dark:text-gray-300">2</button>
            <button class="px-3 py-1 text-sm text-gray-600 dark:text-gray-300">下一页</button>
          </nav>
        </div>
      </div>

      <!-- 侧边栏 -->
      <aside class="space-y-6">
        <div class="bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-lg p-4">
          <h3 class="font-semibold mb-2">关于作者</h3>
          <p class="text-sm text-gray-600 dark:text-gray-400">你好，我是博主，记录技术与成长。如果你喜欢内容，可以订阅或联系我。</p>
        </div>

        <div class="bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-lg p-4">
          <h3 class="font-semibold mb-2">最新文章</h3>
          <ul class="space-y-2 text-sm text-gray-600 dark:text-gray-400">
            <li v-for="a in articles.slice(0,3)" :key="a.id"><a class="hover:underline" @click.prevent="openArticle(a.path)">{{ a.title }}</a></li>
          </ul>
        </div>

        <div class="bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 rounded-lg p-4">
          <h3 class="font-semibold mb-2">分类</h3>
          <div class="flex flex-wrap gap-2">
            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-sm rounded">前端</span>
            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-sm rounded">运维</span>
            <span class="px-2 py-1 bg-gray-100 dark:bg-gray-700 text-sm rounded">写作</span>
          </div>
        </div>
      </aside>
    </div>
  </section>
</template>

<style scoped>
/* 保持文章卡片统一高度（可根据需要移除） */
article {
  min-height: 160px;
}
</style>
