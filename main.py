from src.CSVManage.get_language import generate_csv_column_language
from src.JSONManage.manage_languages import newlanguage
from src.Config.config import ConfigCSV, ConfigJSON
from src.utils.clear_console import clear_console


def generate_language_csv_column(language: str, language_iso: str) -> None:
    csv_path: str = ConfigCSV.csv_path
    generate_csv_column_language(language=language, path=csv_path)


def generate_language_for_json(language: str, language_iso: str) -> None:
    # json_path: str = ConfigJSON.json_path
    json_path: str = (
        "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/EntitiesLanguageJson.json"
    )
    newlanguage(language, language_iso, json_path, False)


clear_console()
generate_language_for_json("Espannol de Espanna", "es_es")
generate_language_for_json("ingles", "en")
# generate_language_for_json("Espannol de Latinoamerica", "es_lt")
# generate_language_for_json("Frances", "fr")
# generate_language_for_json("italiano", "it")
# generate_language_for_json("ruso", "rs")
