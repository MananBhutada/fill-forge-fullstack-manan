FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential
COPY backend/requirements.txt ./requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY backend/ ./
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]