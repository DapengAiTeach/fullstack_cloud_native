<script setup>
import { useUserStore } from '../store/user_store.js'

const userStore = useUserStore()
</script>

<template>
  <section class="container-wrapper py-12 min-h-screen">
    <!-- 页面标题 -->
    <div class="text-center mb-10">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-2">设置</h1>
      <p class="text-lg text-gray-600 dark:text-gray-400">管理您的偏好设置</p>
    </div>

    <div class="max-w-2xl mx-auto space-y-6">
      <!-- 帐户设置 -->
      <el-card>
        <template #header>
          <div class="card-header">
            <span>帐户设置</span>
          </div>
        </template>
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              当前邮箱
            </label>
            <p class="text-gray-900 dark:text-white">{{ userStore.userInfo.email }}</p>
          </div>
          <el-button>更改邮箱</el-button>
        </div>
      </el-card>

      <!-- 隐私设置 -->
      <el-card>
        <template #header>
          <div class="card-header">
            <span>隐私设置</span>
          </div>
        </template>
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <span class="text-gray-700 dark:text-gray-300">公开个人资料</span>
            <el-switch />
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-700 dark:text-gray-300">显示发布的文章</span>
            <el-switch />
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-700 dark:text-gray-300">接收评论通知</span>
            <el-switch v-model="userStore.userPreferences.notificationsEnabled" />
          </div>
        </div>
      </el-card>

      <!-- 安全设置 -->
      <el-card>
        <template #header>
          <div class="card-header">
            <span>安全设置</span>
          </div>
        </template>
        <div class="space-y-4">
          <el-button>修改密码</el-button>
          <el-button>两步验证</el-button>
          <el-button>登出所有设备</el-button>
        </div>
      </el-card>

      <!-- 数据管理 -->
      <el-card>
        <template #header>
          <div class="card-header">
            <span>数据管理</span>
          </div>
        </template>
        <div class="space-y-4">
          <el-button>导出我的数据</el-button>
          <el-button type="danger">删除帐户</el-button>
        </div>
      </el-card>
    </div>
  </section>
</template>

<style scoped>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
