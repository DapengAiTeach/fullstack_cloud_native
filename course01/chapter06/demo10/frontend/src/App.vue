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
  <div>
    <table>
      <thead>
        <tr>
          <th>电影ID</th>
          <th>电影名称</th>
          <th>导演</th>
          <th>主演</th>
          <th>类型</th>
          <th>上映年份</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="movie in movies" :key="movie.id">
          <td>{{ movie.id }}</td>
          <td>{{ movie.title }}</td>
          <td>{{ movie.director }}</td>
          <td>{{ movie.actors }}</td>
          <td>{{ movie.genre }}</td>
          <td>{{ movie.year }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>