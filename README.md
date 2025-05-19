# Taller 2 
Este proyecto consiste en generar un programa el cual nos permita explorar la API sleccionada para poder extraer informacion directamente de esta de una manera mas sencilla y poder verla de una manera mas amigable tambien.

La API a usar fue encontrada en el siguiente link: "https://restcountries.com/"

Se realizo la instalacion con los siguientes 3 comandos:

pip install jupyterlab

pip install nbdev

pip install requests pandas

# API
La api a usar se llama REST Countries.

En la cual se pueden encontrar informacion completa de todos los paises del mundo, tales como: nombre del pais, capital, abreviación, latitud, región, etc.

En este caso usaremos la API para obtener nombre del pais, capital, region, poblacion, area e idiomas y visualizarlos en una tabla de manera mas ordenada.

# Notebook
En el notebook podremos encontrar 3 codigos ejecutables, el primero nos entrega una tabla con nombre del pais, capital, region, poblacion, area e idiomas, de los 100 primeros paises que aparecen en la API.

El segundo codigo nos da la informacion completa que está presente en la API para el pais Chile.

Y por ultimo el tercer codigo nos entrega la misma tabla pero con una columna extra en la que se nos da una breve descripcion de la informacion presente en la fila.

# Significado de las columnas numéricas - `paises_numericos.csv`

| **Columna**            | **Tipo de dato**     | **Significado** |
|------------------------|----------------------|------------------|
| `independent`          | Binario (0/1)        | `1` si el país es independiente, `0` si no lo es o el dato es desconocido. |
| `unMember`             | Binario (0/1)        | `1` si el país es miembro de la ONU, `0` si no lo es. |
| `capital_code`         | Categórico (entero)  | Código único asignado a la capital. `"None"` si no tiene capital registrada. |
| `region_code`          | Categórico (entero)  | Código único para la región geográfica (ej. `Europe` = 1, `Asia` = 2, etc.). |
| `subregion_code`       | Categórico (entero)  | Código único para la subregión (ej. `Northern Europe`, `South America`). |
| `language_code`        | Categórico (entero)  | Código numérico para el idioma o combinación de idiomas oficiales. |
| `latitude`             | Decimal (float)      | Latitud aproximada del país. Positiva = hemisferio norte. |
| `longitude`            | Decimal (float)      | Longitud aproximada del país. Positiva = hemisferio este. |
| `landlocked`           | Binario (0/1)        | `1` si el país no tiene salida al mar, `0` si sí tiene. |
| `area`                 | Decimal (float)      | Área del país en kilómetros cuadrados. |
| `population`           | Entero               | Población total estimada del país. |
| `borders_count`        | Entero               | Cantidad de países con los que comparte frontera. |
| `car_side_code`        | Categórico (entero)  | Código: `1` = "right", `2` = "left", `3` = desconocido. |
| `timezones_count`      | Entero               | Número de zonas horarias que tiene el país. |
| `continents_code`      | Categórico (entero)  | Código del continente (ej. `Africa` = 1, `Europe` = 2). |
| `startOfWeek_code`     | Categórico (entero)  | Día de inicio de semana: `1` = "monday", `2` = "sunday", etc. |
