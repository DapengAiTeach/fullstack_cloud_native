FROM zhangdapeng/fastapi:python3.11.9-slim 

WORKDIR /app

COPY main.py .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]