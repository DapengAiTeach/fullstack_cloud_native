<script setup>
import { useUserStore } from '../store/user_store.js'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

const handleNavigateToArticle = (id) => {
  router.push(`/blog/${id}`)
}
</script>

<template>
  <section class="container-wrapper py-12 min-h-screen">
    <!-- 页面标题 -->
    <div class="text-center mb-10">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-2">我的收藏</h1>
      <p class="text-lg text-gray-600 dark:text-gray-400">
        您已收藏 {{ userStore.favoriteArticles.length }} 篇文章
      </p>
    </div>

    <!-- 未登录提示 -->
    <div v-if="!userStore.isAuthenticated" class="max-w-4xl mx-auto">
      <el-empty description="请先登录" />
    </div>

    <!-- 空状态 -->
    <div v-else-if="userStore.favoriteArticles.length === 0" class="max-w-4xl mx-auto">
      <el-empty description="还没有收藏任何文章" />
    </div>

    <!-- 收藏列表 -->
    <div v-else class="max-w-4xl mx-auto">
      <el-card v-for="id in userStore.favoriteArticles" :key="id" class="mb-4 cursor-pointer hover:shadow-lg transition-shadow">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-2">
              文章 #{{ id }}
            </h3>
            <p class="text-gray-600 dark:text-gray-400">这是您收藏的文章</p>
          </div>
          <div class="flex gap-2">
            <el-button type="primary" @click="handleNavigateToArticle(id)">查看</el-button>
            <el-button @click="userStore.removeFavorite(id)">取消收藏</el-button>
          </div>
        </div>
      </el-card>
    </div>
  </section>
</template>
