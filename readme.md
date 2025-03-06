# JSON & CVS Languages Generator

Un simple generador de idiomas desde archivos `CSV` o Archivos `JSON`. Utilizando la APi de `OpenAI` y el modelo `gpt-4o-mini`.

## Overview
El proyecto es especifico y posee algunas caracteristicas que son inmutables si no se cambian los prompt. Por ejemplo lo que haya dentro de los caracteres `<>` o `{}` no se traducen, se quedan exactamente igual. En caso que se quiera cambiar la forma de procesar los lenguajes, cambiar los prompts en [Config](src/Config/config.py).

## Generacion CSV
En el archivo [`src/CSVManage/get_language.py`](src/CSVManage/get_language.py), se encuentran los metodos para generar nuevas columnas del `.csv`. El metodo `generate_csv_column_language` se encarga de generar una nueva columna en el idioma pasado. 

En el archivo [`src/CSVManage/utils.py`](src/CSVManage/utils.py), el metodo `generate_n_columns_from_languages_list` genera una columna nueva por cada uno de los idiomas que se pasen en el parametro `languages: list`.

### Ejemplo de uso y resultados
............................

## Generacion JSON

## Requirements
El proyecto requiere cada una de las siguientes bibliotecas que se encuentran en el archivo `requirements.txt`:
- pandas

### OpenAI API
Dado que el proyecto usa `LLMs` de OpenAI, es imprescindible usar una cuenta de esta pagando creditos para usar la api de este servicio. Para esto entre a [la pagina oficial]() de OpenAI y siga los pasos para crear una cuenta con este objetivo.

## Recomendaciones
- Intalar la biblioteca [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv") es muy util para visualizar archivos `.csv` en **vsCode**.
- Ajustar cada uno de los prompts a las necesidades de cada cual.
