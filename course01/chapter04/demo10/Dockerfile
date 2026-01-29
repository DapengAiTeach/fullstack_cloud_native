# 基于通用 FastAPI 基础镜像
FROM zhangdapeng520/fastapi:python3.11.9

WORKDIR /app

# 复制项目源码
COPY main.py .

# 暴露应用端口
EXPOSE 8000

# 定义应用启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]