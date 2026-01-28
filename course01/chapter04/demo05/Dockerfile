FROM node:22.22.0-slim

WORKDIR /app

# 安装依赖
COPY package*.json ./
RUN npm config set registry https://registry.npmmirror.com && npm install


# 复制应用代码
COPY server.js ./

# 暴露端口
EXPOSE 3000

# 启动应用
CMD ["npm", "start"]