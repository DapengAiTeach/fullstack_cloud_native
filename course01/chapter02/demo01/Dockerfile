# 使用官方的 Python 镜像
FROM python:3.11-slim
# 设置工作目录
WORKDIR /app
# 复制 server.py 到容器内
COPY server.py .
# 暴露容器端口
EXPOSE 8000
# 运行 Python HTTP 服务器
CMD ["python", "server.py"]