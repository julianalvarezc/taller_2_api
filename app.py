#Importamos la biblioteca
import requests

#Definimos la URL a la que queremos hacer peticiones
url = "https://restcountries.com/v3.1/all"

#Hacemos la peticion y la guardamos en una variable
response = requests.get(url)

#Obtenemos el json de la respuesta
api = response.json()

print(api)