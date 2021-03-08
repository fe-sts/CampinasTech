<h1 align="center">Aplicativo Web para tradução de IA usando Python e Flask</h1>

## Para executar esse projeto é necessário:

Ativar o ambiente virtual
```
.\Scripts\activate
```

## Instalar as bibliotecas necessárias e dependências
```
pip install -r requirements.txt
```

## Seguir as orientações a seguir para obter os dados e preencher o arquivo '.env'

* [Microsoft] https://docs.microsoft.com/pt-br/learn/modules/python-flask-build-ai-web-app/5-exercise-create-translator-service

## Arquivo .env:
```
KEY=your_key
ENDPOINT=your_endpoint
LOCATION=your_location
```

## Em app.py adicionar o import request
```
from flask import Flask, render_template, request
```

## Para executar, use o comando:
```
flask run
```