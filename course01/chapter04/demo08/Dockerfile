# 使用 Node.js v22.22.0 官方稳定版镜像
FROM node:22.22.0-slim

# 设置统一的工作目录
# 所有基于该镜像的 Vue 项目默认在 /app 下工作
WORKDIR /app

# 配置 npm 国内镜像源，提升国内环境下依赖安装的稳定性
# 安装 pnpm，并固定版本，如果团队只使用 npm，可以删除这一段
# 在构建阶段验证 Node 和包管理器版本，用于提前发现环境异常
RUN npm config set registry https://registry.npmmirror.com && npm install -g pnpm@9.0.0 && node -v && npm -v && pnpm -v

# 基础镜像不定义 CMD
# 具体项目自行决定构建与运行方式