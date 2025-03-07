from src.OpenAI.gpt_service import GPT
from src.Config.config import ConfigJSON
import asyncio
import json
from tqdm import tqdm

gpt: GPT = GPT()

base_language_iso = "es"


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

    print(f"\nGENERANDO LENGUAJE {language.upper()}")
    pbar = tqdm(total=len(my_json), dynamic_ncols=True, desc="Generated Language")

    tasks = [
        GenerateValuesForKey(
            language=language,
            language_iso=language_iso,
            key=key,
            my_json=my_json,
            pbar=pbar,
        )
        for key in my_json
    ]
    await asyncio.gather(*tasks)

    with open(path, "w") as file:
        json.dump(my_json, file, indent=4)


MAX_ITER_ON_ERROR = 50


async def GenerateValuesForKey(
    language: str,
    language_iso: str,
    key: str,
    my_json: dict[str, dict],
    pbar: tqdm,
    iteration: int = 0,
    path: str = ConfigJSON.json_path,
):
    try:
        if not my_json[key].__contains__(language_iso) or (
            my_json[key][language_iso]["name"] == ""
            and my_json[key][base_language_iso]["name"] != ""
        ):
            if not my_json[key].__contains__(language_iso):
                my_json[key][language_iso] = {"name": "", "description": ""}

            my_json[key][language_iso]["name"] = await gpt.single_translate(
                language=language, string=my_json[key][base_language_iso]["name"]
            )
        elif my_json[key][base_language_iso]["name"] == "":
            my_json[key][language_iso]["name"] = ""

        if not my_json[key].__contains__(language_iso) or (
            my_json[key][language_iso]["description"] == ""
            and my_json[key][base_language_iso]["description"] != ""
        ):
            my_json[key][language_iso]["description"] = await gpt.single_translate(
                language=language, string=my_json[key][base_language_iso]["description"]
            )
        elif my_json[key][base_language_iso]["description"] == "":
            my_json[key][language_iso]["description"] = ""

        # with open(path, "w") as file:
        #     json.dump(my_json, file, indent=4)

        pbar.set_postfix(api_price=gpt.current_price, refresh=False)
        pbar.update()
    except:
        # Si hay un error como puedo ser timeouterror repetir la funcion cierta cantidad de intentos
        iteration += 1
        await asyncio.sleep(0.5)
        if iteration < MAX_ITER_ON_ERROR:
            await GenerateValuesForKey(
                language, language_iso, key, json, pbar, iteration
            )


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
