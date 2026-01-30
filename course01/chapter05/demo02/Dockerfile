FROM python:3.11.9-slim

WORKDIR /app

# pip 国内源配置
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn \
    && pip install requests

COPY . .

CMD ["python", "service_a.py"]