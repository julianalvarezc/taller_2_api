#Importamos la biblioteca
# src/app.py

import requests

def get_api_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    return response.json()
