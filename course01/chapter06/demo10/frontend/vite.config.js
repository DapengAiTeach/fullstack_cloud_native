import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    proxy: {
      // 请求以 /ch06_demo10_backend 开头的 URL 都会被代理到后端服务器
      '/ch06_demo10_backend': {
        target: 'http://127.0.0.1:8000', // 后端的接口地址
        changeOrigin: true,  // 是否修改请求头中的Origin
        // 重写路径，把 /ch06_demo10_backend 去掉
        rewrite: (path) => path.replace(/^\/ch06_demo10_backend/, ''),  
      },
    },
  },
})
