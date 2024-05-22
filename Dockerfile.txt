# Wybierz obraz bazowy
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki projektu do obrazu
COPY app.py model.pkl requirements.txt ./

# Zainstaluj wymagane biblioteki
RUN pip install --no-cache-dir -r requirements.txt

# Uruchom aplikację
CMD ["python", "app.py"]
