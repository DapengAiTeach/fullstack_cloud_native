import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useUserStore = defineStore('user', () => {
  // 状态
  const userInfo = ref({
    id: null,
    username: '',
    email: '',
    avatar: '',
    isLoggedIn: false
  })

  const userPreferences = ref({
    theme: 'light', // light | dark
    language: 'zh-CN',
    notificationsEnabled: true
  })

  const favoriteArticles = ref([]) // 收藏的文章ID列表

  // 计算属性
  const isAuthenticated = computed(() => userInfo.value.isLoggedIn)
  
  const userDisplayName = computed(() => {
    return userInfo.value.username || '游客用户'
  })

  // 方法
  const login = (username, email, avatar = '') => {
    userInfo.value = {
      id: Date.now(),
      username,
      email,
      avatar: avatar || `https://api.dicebear.com/7.x/avataaars/svg?seed=${username}`,
      isLoggedIn: true
    }
    // 保存到 localStorage
    saveUserToStorage()
  }

  const logout = () => {
    userInfo.value = {
      id: null,
      username: '',
      email: '',
      avatar: '',
      isLoggedIn: false
    }
    favoriteArticles.value = []
    localStorage.removeItem('user_info')
  }

  const updateUserProfile = (updates) => {
    userInfo.value = { ...userInfo.value, ...updates }
    saveUserToStorage()
  }

  const toggleTheme = () => {
    userPreferences.value.theme = 
      userPreferences.value.theme === 'light' ? 'dark' : 'light'
    savePreferencesToStorage()
  }

  const setTheme = (theme) => {
    userPreferences.value.theme = theme
    savePreferencesToStorage()
  }

  const addFavorite = (articleId) => {
    if (!favoriteArticles.value.includes(articleId)) {
      favoriteArticles.value.push(articleId)
      saveFavoritesToStorage()
    }
  }

  const removeFavorite = (articleId) => {
    const index = favoriteArticles.value.indexOf(articleId)
    if (index > -1) {
      favoriteArticles.value.splice(index, 1)
      saveFavoritesToStorage()
    }
  }

  const isFavorited = (articleId) => {
    return favoriteArticles.value.includes(articleId)
  }

  const toggleFavorite = (articleId) => {
    if (isFavorited(articleId)) {
      removeFavorite(articleId)
    } else {
      addFavorite(articleId)
    }
  }

  // 本地存储相关
  const saveUserToStorage = () => {
    localStorage.setItem('user_info', JSON.stringify(userInfo.value))
  }

  const savePreferencesToStorage = () => {
    localStorage.setItem('user_preferences', JSON.stringify(userPreferences.value))
  }

  const saveFavoritesToStorage = () => {
    localStorage.setItem('favorite_articles', JSON.stringify(favoriteArticles.value))
  }

  const loadFromStorage = () => {
    const savedUser = localStorage.getItem('user_info')
    const savedPreferences = localStorage.getItem('user_preferences')
    const savedFavorites = localStorage.getItem('favorite_articles')

    if (savedUser) {
      userInfo.value = JSON.parse(savedUser)
    }
    if (savedPreferences) {
      userPreferences.value = JSON.parse(savedPreferences)
    }
    if (savedFavorites) {
      favoriteArticles.value = JSON.parse(savedFavorites)
    }
  }

  return {
    // 状态
    userInfo,
    userPreferences,
    favoriteArticles,
    // 计算属性
    isAuthenticated,
    userDisplayName,
    // 方法
    login,
    logout,
    updateUserProfile,
    toggleTheme,
    setTheme,
    addFavorite,
    removeFavorite,
    isFavorited,
    toggleFavorite,
    loadFromStorage
  }
})
