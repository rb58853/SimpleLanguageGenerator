from src.OpenAI.gpt_service import GPT
from src.Config.config import ConfigJSON
import asyncio
import json
from tqdm import tqdm

gpt: GPT = GPT()

base_language_iso = "base"


def newlanguage(
    language: str,
    language_iso: str,
    path: str = ConfigJSON.json_path,
    override: bool = False,
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
    asyncio.run(call_new_language(language, language_iso, path, override))


async def call_new_language(
    language: str, language_iso: str, path: str, override: bool
):
    with open(path, "r") as file:
        my_json: dict = json.load(file)

    print(f"\n\nGENERANDO LENGUAJE {language.upper()}")
    pbar = tqdm(total=len(my_json), dynamic_ncols=True, desc="Generated Language")

    tasks = [
        GenerateValuesForKey(
            language=language,
            language_iso=language_iso,
            key=key,
            json=my_json,
            pbar=pbar,
        )
        for key in my_json
    ]
    await asyncio.gather(*tasks)

    with open(path, "w") as file:
        json.dump(my_json, file, indent=4)


async def GenerateValuesForKey(
    language: str, language_iso: str, key: str, json: dict[str, dict], pbar: tqdm
):
    if not json[key].__contains__(language_iso) or (
        json[key][language_iso]["name"] == ""
        and json[key][base_language_iso]["name"] != ""
    ):
        if not json[key].__contains__(language_iso):
            json[key][language_iso] = {"name": "", "description": ""}

        json[key][language_iso]["name"] = await gpt.single_translate(
            language=language, string=json[key][base_language_iso]["name"]
        )
    elif json[key][base_language_iso]["name"] == "":
        json[key][language_iso]["name"] = ""

    if not json[key].__contains__(language_iso) or (
        json[key][language_iso]["description"] == ""
        and json[key][base_language_iso]["description"] != ""
    ):
        json[key][language_iso]["description"] = await gpt.single_translate(
            language=language, string=json[key][base_language_iso]["description"]
        )
    elif json[key][base_language_iso]["description"] == "":
        json[key][language_iso]["description"] = ""

    pbar.set_postfix(api_price=gpt.current_price, refresh=False)
    pbar.update()


def delete_language(language_iso: str, path: str = ConfigJSON.json_path):
    with open(path, "r") as file:
        my_json: dict[str, dict] = json.load(file)

    for key in my_json:
        for iso in my_json[key].keys:
            if iso == language_iso:
                my_json[key].__delitem__(iso)

    with open(path, "w") as file:
        json.dump(my_json, file, indent=4)
    pass
