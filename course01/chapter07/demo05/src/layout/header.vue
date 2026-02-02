<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/store/user_store.js'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()
const isMenuOpen = ref(false)
const windowWidth = ref(0)
const showUserMenu = ref(false)

// 导航菜单数据
const menuItems = ref([
  { label: '首页', path: '/', icon: '🏠' },
  { label: '博客', path: '/blog', icon: '📝' },
  { label: '分类', path: '/categories', icon: '🏷️' },
  { label: '关于', path: '/about', icon: 'ℹ️' },
  { label: '联系', path: '/contact', icon: '📧' },
])

// 判断是否为移动端
const isMobile = computed(() => windowWidth.value < 768)

// 监听窗口大小变化
const handleResize = () => {
  windowWidth.value = window.innerWidth
}

onMounted(() => {
  windowWidth.value = window.innerWidth
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

// 菜单切换
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

// 关闭菜单
const closeMenu = () => {
  isMenuOpen.value = false
}

// 导航到页面
const navigateTo = (path) => {
  router.push(path)
  closeMenu()
}

// 切换主题
const toggleTheme = () => {
  userStore.toggleTheme()
  const html = document.documentElement
  if (userStore.userPreferences.theme === 'dark') {
    html.classList.add('dark')
  } else {
    html.classList.remove('dark')
  }
}

// 登录/登出
const handleLogin = () => {
  if (userStore.isAuthenticated) {
    userStore.logout()
    showUserMenu.value = false
  } else {
    // 模拟登录
    userStore.login('张三', 'zhangsan@example.com')
  }
}

</script>

<template>
  <!-- 头部导航栏 -->
  <header class="sticky top-0 z-50 bg-white dark:bg-gray-900 shadow-md transition-colors duration-300">
    <nav class="container-wrapper">
      <div class="flex items-center justify-between h-16">
        
        <!-- Logo 部分 -->
        <div class="flex-shrink-0 flex items-center">
          <div class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent cursor-pointer hover:from-blue-700 hover:to-cyan-700 transition-all"
               @click="navigateTo('/')">
            📚 MyBlog
          </div>
        </div>

        <!-- 桌面端导航菜单 -->
        <div v-if="!isMobile" class="flex items-center space-x-1">
          <button
            v-for="item in menuItems"
            :key="item.path"
            @click="navigateTo(item.path)"
            :class="[
              'px-3 py-2 rounded-md text-sm font-medium transition-all duration-200',
              route.path === item.path
                ? 'bg-blue-600 text-white'
                : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
            ]"
          >
            <span class="mr-1">{{ item.icon }}</span>
            <span>{{ item.label }}</span>
          </button>
        </div>

        <!-- 右侧功能按钮 -->
        <div class="flex items-center space-x-4">
          <!-- 搜索框 (桌面端) -->
          <div v-if="!isMobile" class="hidden md:flex items-center bg-gray-100 dark:bg-gray-800 rounded-full px-4 py-2">
            <input
              type="text"
              placeholder="搜索文章..."
              class="bg-transparent outline-none text-sm text-gray-700 dark:text-gray-300 placeholder-gray-500 dark:placeholder-gray-400 w-40"
            />
            <span class="ml-2 text-gray-400">🔍</span>
          </div>

          <!-- 主题切换按钮 -->
          <button
            @click="toggleTheme"
            class="p-2 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
            title="切换主题"
          >
            <span class="text-xl">{{ userStore.userPreferences.theme === 'dark' ? '☀️' : '🌙' }}</span>
          </button>

          <!-- 用户菜单 -->
          <div class="relative">
            <button
              @click="showUserMenu = !showUserMenu"
              class="flex items-center space-x-2 px-3 py-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
              title="用户菜单"
            >
              <img
                v-if="userStore.isAuthenticated"
                :src="userStore.userInfo.avatar"
                :alt="userStore.userDisplayName"
                class="w-8 h-8 rounded-full"
              />
              <span v-else class="text-xl">👤</span>
              <span class="hidden md:inline text-sm text-gray-700 dark:text-gray-300">
                {{ userStore.userDisplayName }}
              </span>
            </button>

            <!-- 用户菜单下拉框 -->
            <div
              v-if="showUserMenu"
              class="absolute right-0 mt-2 w-48 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 overflow-hidden z-50"
            >
              <div class="px-4 py-3 border-b border-gray-200 dark:border-gray-700">
                <p class="text-sm font-semibold text-gray-900 dark:text-white">
                  {{ userStore.userDisplayName }}
                </p>
                <p v-if="userStore.isAuthenticated" class="text-xs text-gray-500 dark:text-gray-400">
                  {{ userStore.userInfo.email }}
                </p>
              </div>

              <div v-if="userStore.isAuthenticated" class="py-2">
                <button
                  @click="() => { router.push('/profile'); showUserMenu = false }"
                  class="w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  👤 个人资料
                </button>
                <button
                  @click="() => { router.push('/favorites'); showUserMenu = false }"
                  class="w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  ❤️ 我的收藏 ({{ userStore.favoriteArticles.length }})
                </button>
                <button
                  @click="() => { router.push('/settings'); showUserMenu = false }"
                  class="w-full text-left px-4 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700"
                >
                  ⚙️ 设置
                </button>
              </div>

              <div class="border-t border-gray-200 dark:border-gray-700 py-2">
                <button
                  @click="handleLogin"
                  class="w-full text-left px-4 py-2 text-sm font-semibold transition-colors"
                  :class="userStore.isAuthenticated
                    ? 'text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20'
                    : 'text-green-600 dark:text-green-400 hover:bg-green-50 dark:hover:bg-green-900/20'"
                >
                  {{ userStore.isAuthenticated ? '📴 登出' : '🔐 登录' }}
                </button>
              </div>
            </div>
          </div>

          <!-- 关闭用户菜单（点击其他地方） -->
          <div
            v-if="showUserMenu"
            @click="showUserMenu = false"
            class="fixed inset-0 z-40"
          />

          <!-- 汉堡菜单按钮 (移动端) -->
          <button
            v-if="isMobile"
            @click="toggleMenu"
            class="p-2 rounded-md text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            :aria-expanded="isMenuOpen"
            aria-label="打开菜单"
          >
            <svg
              class="w-6 h-6 transition-transform duration-300"
              :class="{ 'rotate-90': isMenuOpen }"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
            </svg>
          </button>
        </div>
      </div>

      <!-- 移动端下拉菜单 -->
      <div
        v-if="isMobile && isMenuOpen"
        class="overflow-hidden transition-all duration-300 ease-in-out"
      >
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 border-t border-gray-200 dark:border-gray-700">
          
          <!-- 移动端搜索框 -->
          <div class="px-2 py-2 mb-2">
            <input
              type="text"
              placeholder="搜索文章..."
              class="w-full px-4 py-2 rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 placeholder-gray-500 dark:placeholder-gray-400 outline-none focus:ring-2 focus:ring-blue-600"
            />
          </div>

          <!-- 移动端菜单项 -->
          <button
            v-for="item in menuItems"
            :key="item.path"
            @click="navigateTo(item.path)"
            :class="[
              'w-full text-left px-3 py-2 rounded-md text-base font-medium transition-colors duration-200',
              route.path === item.path
                ? 'bg-blue-600 text-white'
                : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800'
            ]"
          >
            <span class="mr-2">{{ item.icon }}</span>
            <span>{{ item.label }}</span>
          </button>

          <!-- 移动端用户菜单 -->
          <div v-if="userStore.isAuthenticated" class="border-t border-gray-200 dark:border-gray-700 pt-2 mt-2">
            <div class="px-3 py-2 text-sm font-semibold text-gray-700 dark:text-gray-300">
              {{ userStore.userDisplayName }}
            </div>
            <button
              @click="() => { router.push('/profile'); closeMenu() }"
              class="w-full text-left px-3 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-md"
            >
              👤 个人资料
            </button>
            <button
              @click="() => { router.push('/favorites'); closeMenu() }"
              class="w-full text-left px-3 py-2 text-sm text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-md"
            >
              ❤️ 我的收藏 ({{ userStore.favoriteArticles.length }})
            </button>
            <button
              @click="handleLogin"
              class="w-full text-left px-3 py-2 text-sm font-semibold text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-md mt-2"
            >
              📴 登出
            </button>
          </div>

          <div v-else class="border-t border-gray-200 dark:border-gray-700 pt-2 mt-2">
            <button
              @click="handleLogin"
              class="w-full text-left px-3 py-2 text-sm font-semibold text-green-600 dark:text-green-400 hover:bg-green-50 dark:hover:bg-green-900/20 rounded-md"
            >
              🔐 登录
            </button>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<style scoped>
/* 主题过渡动画 */
:deep(html) {
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* 菜单动画 */
.v-enter-active,
.v-leave-active {
  transition: all 0.3s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>