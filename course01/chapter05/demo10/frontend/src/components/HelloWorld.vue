<script setup>
import { onMounted, ref } from 'vue'
import { fetchItems } from "@/api"

defineProps({
  msg: String,
})


// 定义响应式变量
const items = ref([])

// 在页面加载时自动执行
onMounted(async () => {
  console.log('会在页面加载的时候自动执行')
  // 接口请求代码一般都是放在这里面的
  const res = await fetchItems()
  console.log('获取到的商品列表数据：', res)
  // 将获取到的数据赋值给响应式变量
  items.value = res
})
</script>

<template>
  <h1>{{ msg }}</h1>
  <hr>
  <div>
    <h3>欢迎使用商品管理系统</h3>
    <!-- 使用for循环遍历商品列表并展示 -->
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.id }} - {{ item.name }} - ￥{{ item.price }}
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>
