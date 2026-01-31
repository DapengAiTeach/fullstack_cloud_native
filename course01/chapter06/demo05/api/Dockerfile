FROM zhangdapeng520/fastapi:python3.11.9-slim

WORKDIR /app

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]