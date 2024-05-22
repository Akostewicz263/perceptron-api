
FROM python:3.9-slim

WORKDIR /app

COPY app.py model.pkl requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]