# 使用明确版本的 Node.js 基础镜像
FROM node:22.22.0-slim

# 设置容器内工作目录
WORKDIR /app

# 复制应用代码到容器
COPY app.js .

# 定义容器启动命令
CMD ["node", "app.js"]