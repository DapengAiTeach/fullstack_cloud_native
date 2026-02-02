<script setup>
import { ElButton, ElConfigProvider } from "element-plus";
import zhCn from "element-plus/es/locale/lang/zh-cn";
import "dayjs/locale/zh-cn";
</script>

<template>
  <div>
    <el-config-provider :locale="zhCn">
      <div>
        <h1 class="text-3xl font-bold underline bg-blue-500">Hello world!</h1>
        <el-button type="primary">Element Plus 按钮</el-button>
      </div>
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
