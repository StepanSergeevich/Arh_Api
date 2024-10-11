
FROM python:3.9-slim


WORKDIR /app


COPY . .


RUN pip install --no-cache-dir -r requirements.txt


ENV POSTGRES_HOST="127.0.0.1"
ENV POSTGRES_USER="postgres"
ENV POSTGRES_PASSWORD="123"
ENV POSTGRES_DB="api_database"


CMD ["python", "app.py"]