FROM python:3.11-slim

WORKDIR /app

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && pip install --no-cache-dir fastapi uvicorn

COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]