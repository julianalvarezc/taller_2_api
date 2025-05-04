#Importamos la biblioteca
import requests

#Definimos la URL a la que queremos hacer peticiones
url = "https://restcountries.com/v3.1/lang/spanish"

#Hacemos la peticion y la guardamos en una variable
response = requests.get(url)

#Obtenemos el json de la respuesta
response.json()
a = response.json()

print(a)