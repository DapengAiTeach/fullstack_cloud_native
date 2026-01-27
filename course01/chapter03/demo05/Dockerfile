FROM python:3.11-slim

WORKDIR /app

# 不生成.pyc文件
ENV PYTHONDONTWRITEBYTECODE=1
# 日志直接输出到终端
ENV PYTHONUNBUFFERED=1

# 安装依赖
COPY requirements.txt .
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install --no-cache-dir -r requirements.txt

# 复制源码
COPY . .

# 收集静态文件
RUN python manage.py collectstatic --noinput

# 启动服务
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]