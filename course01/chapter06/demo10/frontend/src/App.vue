<script setup>
import { ref, onMounted } from "vue";
import { fetchMovieList } from "@/api/movie";

// 电影列表数据
const movies = ref([]);
// 搜索关键词
const keyword = ref("");

// 组件挂载时加载电影列表
onMounted(async () => {
  movies.value = await fetchMovieList();
  console.log(movies.value);
});
</script>
<template>
  <div class="page">
    <table class="movie-table">
      <thead>
        <tr>
          <th>电影ID</th>
          <th>电影名称</th>
          <th>导演</th>
          <th>类型</th>
          <th>上映年份</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="movie in movies" :key="movie.id">
          <td>{{ movie.id }}</td>
          <td class="title">{{ movie.title }}</td>
          <td>{{ movie.director }}</td>
          <td>
            <span class="tag">{{ movie.genre }}</span>
          </td>
          <td>{{ movie.release_year }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<style scoped>
/* 页面整体 */
.page {
  padding: 32px;
  background: #f5f7fb;
  min-height: 100vh;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", sans-serif;
}

/* 表格容器 */
.movie-table {
  width: 100%;
  border-collapse: collapse;
  background: #ffffff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
}

/* 表头 */
.movie-table thead {
  background: linear-gradient(135deg, #4f46e5, #6366f1);
}

.movie-table th {
  padding: 14px 16px;
  color: #ffffff;
  font-weight: 600;
  text-align: left;
  font-size: 14px;
  letter-spacing: 0.5px;
}

/* 表体 */
.movie-table tbody tr {
  transition: background-color 0.25s ease, transform 0.15s ease;
}

.movie-table tbody tr:nth-child(even) {
  background-color: #fafafa;
}

.movie-table tbody tr:hover {
  background-color: #eef2ff;
}

/* 单元格 */
.movie-table td {
  padding: 14px 16px;
  font-size: 14px;
  color: #374151;
  border-bottom: 1px solid #e5e7eb;
  vertical-align: middle;
}

/* 电影名称突出 */
.movie-table td.title {
  font-weight: 600;
  color: #111827;
}

/* 类型标签 */
.tag {
  display: inline-block;
  padding: 4px 10px;
  font-size: 12px;
  border-radius: 999px;
  background: #e0e7ff;
  color: #4338ca;
  font-weight: 500;
}

/* 最后一行去掉下边框 */
.movie-table tbody tr:last-child td {
  border-bottom: none;
}

/* 响应式（小屏） */
@media (max-width: 768px) {
  .movie-table {
    font-size: 12px;
  }

  .movie-table th,
  .movie-table td {
    padding: 10px 8px;
  }
}
</style>
