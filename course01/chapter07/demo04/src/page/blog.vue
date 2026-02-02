<script setup>
import { ref } from 'vue'

const posts = ref([
  { 
    id: 1, 
    title: 'Vue3 学习笔记', 
    desc: '记录从零入门 Vue3 的过程',
    category: '前端',
    date: '2024-01-15',
    views: 1205,
    likes: 85
  },
  { 
    id: 2, 
    title: 'Docker 网络理解', 
    desc: '从工程角度理解容器通信',
    category: '运维',
    date: '2024-01-10',
    views: 892,
    likes: 45
  },
  { 
    id: 3, 
    title: '前端工程实践', 
    desc: '组件、状态与样式的协作方式',
    category: '前端',
    date: '2024-01-05',
    views: 2341,
    likes: 156
  }
])

// 方案一：卡片网格布局
</script>

<template>
  <div class="blog-container">
    <div class="blog-header">
      <h1>博客文章</h1>
      <p>分享技术见解与实践经验</p>
    </div>

    <div class="cards-grid">
      <el-card v-for="post in posts" :key="post.id" class="post-card" shadow="hover">
        <template #header>
          <div class="card-header">
            <span class="category-tag">{{ post.category }}</span>
            <span class="post-date">{{ post.date }}</span>
          </div>
        </template>
        
        <div class="post-content">
          <h3 class="post-title">{{ post.title }}</h3>
          <p class="post-desc">{{ post.desc }}</p>
          
          <div class="post-stats">
            <span><i class="el-icon-view"></i> {{ post.views }}</span>
            <span><i class="el-icon-thumb"></i> {{ post.likes }}</span>
          </div>
        </div>

        <template #footer>
          <el-button type="primary" link>阅读更多</el-button>
        </template>
      </el-card>
    </div>
  </div>
</template>

<style scoped>
.blog-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.blog-header {
  text-align: center;
  margin-bottom: 40px;
}

.blog-header h1 {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
}

.blog-header p {
  font-size: 16px;
  color: #666;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
}

.post-card {
  border: 1px solid #f0f0f0;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.post-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1) !important;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.category-tag {
  background: #e6f2ff;
  color: #1890ff;
  padding: 4px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

.post-date {
  color: #999;
  font-size: 12px;
}

.post-content {
  padding: 16px 0;
}

.post-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
  color: #333;
  line-height: 1.4;
}

.post-desc {
  color: #666;
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-stats {
  display: flex;
  gap: 16px;
  color: #999;
  font-size: 13px;
}

.post-stats span {
  display: flex;
  align-items: center;
  gap: 4px;
}
</style>