<script setup>
import { ElConfigProvider } from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import 'dayjs/locale/zh-cn'

import login from '@/page/login.vue';
</script>

<template>
  <div>
    <el-config-provider :locale="zhCn">
      <login />
    </el-config-provider>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
