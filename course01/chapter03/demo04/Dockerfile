FROM node:22.22.0 AS builder

WORKDIR /app

# 安装依赖
COPY package.json ./
RUN npm config set registry https://registry.npmmirror.com && npm install

# 构建静态源码
COPY . .
RUN npm run build


# 运行阶段
FROM nginx:1.26

# 复制nginx的配置文件
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 复制静态HTML源码
COPY --from=builder /app/dist /usr/share/nginx/html