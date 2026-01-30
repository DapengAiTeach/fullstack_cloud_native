<script setup>
import { ref } from "vue"
import { registerUser, loginUser } from "@/api"

// 用户相关变量
const username = ref("")
const password = ref("")

// 消息
const message = ref("")

// 处理注册请求
const handleRegister = async () => {
  try {
    const response = await registerUser(
      username.value,
      password.value
    )
    message.value = "注册成功！"
  } catch (error) {
    message.value = `注册失败: ${error.response.data.detail}`
  }
}

// 处理登录请求
const handleLogin = async () => {
  try {
    const response = await loginUser(
      username.value,
      password.value
    )
    message.value = "登录成功！"
  } catch (error) {
    message.value = `登录失败: ${error.response.data.detail}`
  }
}
</script>

<template>
  <div class="container">
    <h1>用户注册与登录</h1>
    <div class="form-group">
      <label>用户名:</label>
      <input v-model="username" type="text" />
    </div>
    <div class="form-group">
      <label>密码:</label>
      <input v-model="password" type="password" />
    </div>
    <button @click="handleRegister">注册</button>
    <button @click="handleLogin">登录</button>
    <p>{{ message }}</p>
  </div>
</template>

<style scoped>
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
</style>
