from src.Config.config import ConfigGPT, ConfigCSV, ConfigJSON
from openai import OpenAI, AsyncOpenAI
import json

class GPT:
    """
    ## GPT
    GPT es usado para realizar servicios a la api de gpt openAI.
    #### inputs:
    - `model`: modelo de gpt que se utilizara
    """

    def __init__(
        self,
        model=ConfigGPT.DEFAULT_MODEL_NAME,
    ):
        self.client = OpenAI(
            api_key=ConfigGPT.OPENAI_API_KEY,
        )

        self.asyncclient = AsyncOpenAI(
            api_key=ConfigGPT.OPENAI_API_KEY,
        )
        self.model = model
        self.current_price = 0

    def strings_list_to_laguage(self, language: str, words_list: str) -> list:
        """ """

        system_message: str = ConfigCSV.system_prompt

        get_language_message: str = (
            f"Crea una lista en el lenguage {language} usando como base: {words_list}"
        )

        messages: dict = [{"role": "user", "content": get_language_message}]
        messages.insert(0, {"role": "system", "content": system_message})

        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={"type": "json_object"},
        )
        resoponse = completion.choices[0].message.content
        end_list: list = json.loads(resoponse)["list"]
        return end_list


    async def single_translate(self, language: str, string: str) -> str:
        """
        Se le pasa el lenguage y el string que se quiere traducir. Devuelve el string traducido. Ademas agrega el costo de esta operacion al `self.current_price`
        """
        system_message: str = ConfigJSON.system_prompt

        get_language_message: str = (
            f"Traduce al lenguage {language} la siguiente frase: {string}"
        )

        messages: dict = [{"role": "user", "content": get_language_message}]
        messages.insert(0, {"role": "system", "content": system_message})

        completion = await self.asyncclient.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        resoponse = completion.choices[0].message.content
        self.get_price(completion.usage)
        return resoponse
        # return {"price": "0.00", "value": resoponse}

    def get_price(self, usage):
        """
        ## `def` get_price
        recibe el uso de la api y calcula el precio del uso del llamado actua a la api, usando los valores de precio dado por la documentacion oficial de openAI. Ademas aumenta el precio actual usado por la instacia de `class GPT`

        ### inputs:
            - `usage`: uso de la api retornado en el completion respuesta del llamado a la api de gpt
        ### outputs:
            - `price`: precio final del llamado a la api.
        """

        input_tokens = usage.prompt_tokens
        output_tokens = usage.completion_tokens

        input_price = ConfigGPT.MODEL_PRICE[self.model]["input"]
        output_price = ConfigGPT.MODEL_PRICE[self.model]["output"]
        price = input_tokens * input_price + output_tokens * output_price

        self.current_price += price
        return price
