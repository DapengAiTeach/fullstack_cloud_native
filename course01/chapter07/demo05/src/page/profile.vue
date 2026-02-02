<script setup>
import { useUserStore } from '../store/user_store.js'
import { ref } from 'vue'

const userStore = useUserStore()
const isEditing = ref(false)
const editForm = ref({
  username: userStore.userInfo.username,
  email: userStore.userInfo.email
})

const handleSave = () => {
  userStore.updateUserProfile({
    username: editForm.value.username,
    email: editForm.value.email
  })
  isEditing.value = false
  ElMessage.success('个人资料已更新')
}

const handleCancel = () => {
  editForm.value = {
    username: userStore.userInfo.username,
    email: userStore.userInfo.email
  }
  isEditing.value = false
}
</script>

<template>
  <section class="container-wrapper py-12 min-h-screen">
    <!-- 页面标题 -->
    <div class="text-center mb-10">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-white mb-2">个人资料</h1>
      <p class="text-lg text-gray-600 dark:text-gray-400">管理您的账户信息</p>
    </div>

    <!-- 未登录提示 -->
    <div v-if="!userStore.isAuthenticated" class="max-w-2xl mx-auto">
      <el-empty description="请先登录" />
      <div class="text-center mt-4">
        <el-button type="primary">登录账户</el-button>
      </div>
    </div>

    <!-- 用户信息卡片 -->
    <div v-else class="max-w-2xl mx-auto">
      <el-card class="mb-6">
        <!-- 用户头像 -->
        <div class="flex flex-col items-center mb-6">
          <img
            :src="userStore.userInfo.avatar"
            :alt="userStore.userInfo.username"
            class="w-24 h-24 rounded-full border-4 border-blue-600 mb-4"
          />
          <h2 class="text-2xl font-bold text-gray-900 dark:text-white">
            {{ userStore.userInfo.username }}
          </h2>
          <p class="text-gray-600 dark:text-gray-400">{{ userStore.userInfo.email }}</p>
        </div>

        <!-- 基本信息 -->
        <div class="space-y-4">
          <div v-if="!isEditing" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                用户名
              </label>
              <p class="text-gray-900 dark:text-white">{{ userStore.userInfo.username }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                邮箱
              </label>
              <p class="text-gray-900 dark:text-white">{{ userStore.userInfo.email }}</p>
            </div>
            <div class="pt-4">
              <el-button type="primary" @click="isEditing = true">编辑信息</el-button>
            </div>
          </div>

          <!-- 编辑模式 -->
          <div v-else class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                用户名
              </label>
              <el-input v-model="editForm.username" placeholder="输入用户名" />
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                邮箱
              </label>
              <el-input v-model="editForm.email" type="email" placeholder="输入邮箱" />
            </div>
            <div class="flex gap-2 pt-4">
              <el-button type="primary" @click="handleSave">保存</el-button>
              <el-button @click="handleCancel">取消</el-button>
            </div>
          </div>
        </div>
      </el-card>

      <!-- 统计信息 -->
      <el-card class="mb-6">
        <template #header>
          <div class="card-header">
            <span>统计信息</span>
          </div>
        </template>
        <el-row :gutter="20">
          <el-col :xs="24" :sm="8">
            <div class="text-center p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
              <div class="text-3xl font-bold text-blue-600 dark:text-blue-400">
                {{ userStore.favoriteArticles.length }}
              </div>
              <div class="text-sm text-gray-600 dark:text-gray-400">收藏文章</div>
            </div>
          </el-col>
          <el-col :xs="24" :sm="8">
            <div class="text-center p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
              <div class="text-3xl font-bold text-green-600 dark:text-green-400">12</div>
              <div class="text-sm text-gray-600 dark:text-gray-400">发布文章</div>
            </div>
          </el-col>
          <el-col :xs="24" :sm="8">
            <div class="text-center p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
              <div class="text-3xl font-bold text-purple-600 dark:text-purple-400">156</div>
              <div class="text-sm text-gray-600 dark:text-gray-400">获赞数</div>
            </div>
          </el-col>
        </el-row>
      </el-card>

      <!-- 用户偏好设置 -->
      <el-card>
        <template #header>
          <div class="card-header">
            <span>偏好设置</span>
          </div>
        </template>
        <div class="space-y-4">
          <div class="flex items-center justify-between">
            <span class="text-gray-700 dark:text-gray-300">主题</span>
            <el-button-group>
              <el-button
                :type="userStore.userPreferences.theme === 'light' ? 'primary' : 'default'"
                @click="userStore.setTheme('light')"
              >
                ☀️ 亮色
              </el-button>
              <el-button
                :type="userStore.userPreferences.theme === 'dark' ? 'primary' : 'default'"
                @click="userStore.setTheme('dark')"
              >
                🌙 暗色
              </el-button>
            </el-button-group>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-700 dark:text-gray-300">语言</span>
            <el-select v-model="userStore.userPreferences.language" style="width: 200px">
              <el-option label="简体中文" value="zh-CN" />
              <el-option label="English" value="en-US" />
            </el-select>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-gray-700 dark:text-gray-300">接收通知</span>
            <el-switch v-model="userStore.userPreferences.notificationsEnabled" />
          </div>
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
