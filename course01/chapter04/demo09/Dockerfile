# 使用明确版本的 Python 官方镜像
# FROM python:3.11.9
FROM python:3.11.9-slim

# 设置容器内统一工作目录
WORKDIR /app

# 配置 pip 国内镜像源
# 提升国内环境下依赖安装的稳定性
# 升级 pip，避免旧版本带来的兼容问题
# 安装 FastAPI 运行所需的基础依赖，这里只放“所有项目都会用到的内容”
# 验证 Python 与关键依赖版本
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --upgrade pip && \
    pip install fastapi==0.110.0 && \
    pip install uvicorn==0.29.0 && \
    python --version && pip --version

# 基础镜像不定义 CMD
# 具体项目自行决定如何启动应用