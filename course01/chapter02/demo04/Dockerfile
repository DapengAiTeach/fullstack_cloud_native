FROM python:3.11-slim

WORKDIR /app

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && pip install numpy

COPY average_score.py .

CMD ["python", "average_score.py"]