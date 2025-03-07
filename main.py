from src.CSVManage.get_language import generate_csv_column_language
from src.JSONManage.manage_languages import newlanguage
from src.Config.config import ConfigCSV, ConfigJSON
from src.utils.clear_console import clear_console


def generate_language_csv_column(language: str, language_iso: str) -> None:
    csv_path: str = ConfigCSV.csv_path
    generate_csv_column_language(language=language, path=csv_path)


def generate_language_for_json(language: str, language_iso: str) -> None:
    json_path: str = ConfigJSON.json_path
    newlanguage(language, language_iso, json_path, False)

clear_console()
generate_language_for_json("Espannol de espanna", "es-es")
generate_language_for_json("Espannol de latinoamerica", "es-lt")
generate_language_for_json("Frances", "fr")
generate_language_for_json("Italiano", "it")
generate_language_for_json("ruso", "rs")
