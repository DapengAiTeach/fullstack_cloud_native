FROM zhangdapeng520/fastapi:python3.11.9-slim

WORKDIR /app
RUN pip install requests

COPY main.py .
EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0", "--port", "8001"]