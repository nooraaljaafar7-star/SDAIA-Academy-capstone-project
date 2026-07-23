FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run DB setup during build phase so it doesn't delay startup
RUN python setup_db.py

EXPOSE 8000
EXPOSE 7860

CMD ["python", "app_ui.py"]