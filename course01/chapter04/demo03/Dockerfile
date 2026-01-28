FROM node:22.22.0-slim

WORKDIR /app

# 安装依赖
COPY package*.json ./
RUN npm install

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 3000

# 启动服务
CMD ["npm", "run", "start"]