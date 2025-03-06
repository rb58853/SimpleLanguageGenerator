from src.Config.config import ConfigGPT, ConfigCSV
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
