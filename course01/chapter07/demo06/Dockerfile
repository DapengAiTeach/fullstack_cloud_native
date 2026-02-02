# 使用官方 Node.js 镜像进行构建
FROM zhangdapeng520/vue:node22.22.0-slim AS build-stage

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json
COPY package*.json ./

# 安装依赖
RUN pnpm install

# 复制源代码
COPY . .

# 构建 Vue 项目
RUN pnpm run build

# 使用 Nginx 镜像作为生产环境
FROM nginx:1.26-alpine AS production-stage

# 复制构建好的文件到 Nginx 的 html 目录
COPY --from=build-stage /app/dist /usr/share/nginx/html

# 复制自定义的 nginx.conf 到容器中
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 暴露 80 端口
EXPOSE 80

# 启动 Nginx
CMD ["nginx", "-g", "daemon off;"]
