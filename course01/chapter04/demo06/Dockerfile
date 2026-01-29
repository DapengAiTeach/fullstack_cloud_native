# 第一阶段：构建阶段
FROM node:22.22.0 AS build_stage

WORKDIR /app

# 复制构建所需文件
COPY package.json .
COPY index.js .

# 执行构建脚本
RUN npm run build

# 第二阶段：运行阶段
FROM node:22.22.0-slim AS runtime_stage

WORKDIR /app

# 只复制构建产物
COPY --from=build_stage /app/dist ./dist

# 定义启动命令
CMD ["node", "dist/index.js"]