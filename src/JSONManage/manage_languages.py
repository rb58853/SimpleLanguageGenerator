from src.OpenAI.gpt_service import GPT
import asyncio

gpt: GPT = GPT()

base_language_iso = "es"


def newlanguage(language: str, language_iso: str, path: str, override: bool = False):
    asyncio.run(call_new_language(language, language_iso, path, override))


async def call_new_language(
    language: str, language_iso: str, path: str, override: bool = False
):
    """
    ## `new_language`
    Genera todos los valores para un nuevo lenguaje para JSON es de la forma:
    ```
    dict<"key":str, dict<"name||description":str,"value":str>
    ```

    ### INPUTS
    - `language:str`: lenguage que se desea generar.
    - `language_iso:str`: ISO del lenguage que tendra en el JSON. Por ejemplo de 'English' es `'en'`.
    - `path:str`: direccion del archivo `.json` que se desea modificar.
    - `override:bool`: se usa para sobreescribir datos del json. Si es falso solo generara los textos que falten del idioma dado.
    """

    json: dict = None

    count: int = 0


async def GenerateValuesForKey(
    language: str, language_iso: str, key: str, json: dict[str, dict]
):
    if not json[key].__contains__(key=language_iso) or (
        json[key][language_iso]["name"] == ""
        and json[key][base_language_iso]["name"] != ""
    ):
        json[key][language_iso]["name"] = await gpt.single_translate(
            language=language, string=json[key][base_language_iso]["name"]
        )

    if not json[key].__contains__(key=language_iso) or (
        json[key][language_iso]["description"] == ""
        and json[key][base_language_iso]["description"] != ""
    ):
        json[key][language_iso]["description"] = await gpt.single_translate(
            language=language, string=json[key][base_language_iso]["description"]
        )
