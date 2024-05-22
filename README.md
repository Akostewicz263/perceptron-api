# Perceptron Model API

Ten projekt demonstruje, jak wdrożyć model Perceptron za pomocą Flask i Docker.

## Uruchomienie lokalne

1. Zainstaluj zależności: `pip install -r requirements.txt`
2. Uruchom aplikację: `python app.py`

## Uruchomienie w Docker

1. Zbuduj obraz Docker: `docker build -t perceptron-api .`
2. Uruchom kontener: `docker run -p 5000:5000 perceptron-api`
