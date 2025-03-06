import os
import json


class ConfigGPT:
    MODEL_PRICE = {
        "gpt-3.5-turbo": {
            "input": 0.5 / 1000000,
            "output": 1.5 / 1000000,
        },
        "gpt-4o-mini": {
            "input": 0.15 / 1000000,
            "output": 0.60 / 1000000,
        },
    }
    """Precio por cada token utilizado segun el modelo"""

    TOKENS_PER_USD = 1000000

    DEFAULT_MODEL_NAME = "gpt-4o-mini"
    """Modelo default de gpt que se usara"""

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    """Api Key de OpenAI"""


class ConfigCSV:
    system_prompt: str = (
        'Eres un experto en lenguajes. Tu tarea es dado un lenguaje y una lista de string, devolver la propia lista con nuevo lenguage pedido. Devuelve un formato json de la forma {"list": [lista de cada string en el nuevo lenguage]}. Es muy importante que cualquier termino encerrado entre <> lo mantengas exactamente igual, son palabras claves, pero solo si estan contenidas dentro de los signos <> o dentro de los signos {}, respeta los signos y no los cambies. Puede pasar que haya codigo html como <b>Texto</b>, en este caso no puedes traducir <b> ni </b> pero si debes traducir la palabra "Texto" que esta contenida entre <b> y </b>.'
    )
    """
    Prompt de sistema que se le pasa a gpt4-o-mini para generar N nuevas columnas del csv con otro idioma
    """

    batch_size: int = 100
    """Tamanno del batch que se usa para cara iteracion de generacion de strings"""
    # Poner un batch muy alto puede dar error a la hora d generar lenguajes por mala comprension de GPT y un batch muy bajo seria un proceso mas lento. `Default: 100`

    csv_path: str = os.path.sep.join([os.getcwd(), "Data", "my_csv_file.csv"])
    """Direccion default del archivo `CSV`"""


class ConfigJSON:
    system_prompt: str = (
        'Eres un experto en lenguajes. Tu tarea es dado un lenguaje y una frase u oracion, traducir esta al lenguage especificado. Es muy importante que cualquier termino encerrado entre los signos <> o los signos {}, lo mantengas exactamente igual, son palabras claves. Puede pasar que haya codigo html como <b>Texto</b>, en este caso no puedes traducir <b> ni </b> pero si debes traducir la palabra "Texto" que esta contenida entre <b> y </b>.'
    )
    """
    Prompt de sistema que se le pasa a gpt4-o-mini para una traduccion simple respetando las especificidades
    """

    csv_path: str = os.path.sep.join([os.getcwd(), "Data", "my_json_file.csv"])
    """Direccion default del archivo `JSON`"""
