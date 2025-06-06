from src.CSVManage.get_language import generate_csv_column_language
from src.CSVManage.get_characters import get_characters_from_language
from src.CSVManage.utils import delete_Kth_last_columns
from src.JSONManage.manage_languages import (
    newlanguage,
    delete_language,
    get_characters_from_laguage as get_characters_from_laguage_json,
)
from src.Config.config import ConfigCSV, ConfigJSON
from src.utils.clear_console import clear_console


def generate_language_csv_column(language: str, language_iso: str) -> None:
    csv_path: str = ConfigCSV.csv_path
    generate_csv_column_language(language=language, path=csv_path)


def generate_all_json_to_language(language: str, language_iso: str) -> None:
    # Entidades
    print("Entidades".upper(), end="\n")
    json_path: str = (
        "/media/rb58853/d1964fe0-512e-4389-b8f7-b1bd04e82961/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/EntitiesLanguageJson.json"
    )
    newlanguage(language, language_iso, json_path, False, simple=False)
    print("\n\n")

    # Eventos
    print("Eventos".upper(), end="\n")
    json_path: str = (
        "/media/rb58853/d1964fe0-512e-4389-b8f7-b1bd04e82961/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/EventsLanguageJson.json"
    )
    newlanguage(language, language_iso, json_path, False, simple=False)
    print("\n\n")

    # Efectos de eventos
    print("Efectos de Eventos".upper(), end="\n")
    json_path: str = (
        "/media/rb58853/d1964fe0-512e-4389-b8f7-b1bd04e82961/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/EventEffectsLanguageJson.json"
    )
    newlanguage(language, language_iso, json_path, False, simple=False)
    print("\n\n")

    # Textos estaticos
    print("Textos estaticos".upper(), end="\n")
    json_path: str = (
        "/media/rb58853/d1964fe0-512e-4389-b8f7-b1bd04e82961/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/StaticTexts.json"
    )
    newlanguage(language, language_iso, json_path, False, simple=True)
    print("\n\n")


def delete_one_language(language_iso):
    # Entidades
    json_path: str = (
        "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/EntitiesLanguageJson.json"
    )
    delete_language(language_iso, json_path)
    # Eventos
    json_path: str = (
        "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/EventsLanguageJson.json"
    )
    delete_language(language_iso, json_path)

    # Efectos de eventos
    json_path: str = (
        "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/EventEffectsLanguageJson.json"
    )
    delete_language(language_iso, json_path)

    # Textos estaticos
    json_path: str = (
        "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/StaticTexts.json"
    )
    delete_language(language_iso, json_path)


def get_characters(csv_language: str, iso: str):
    characters = get_characters_from_language(csv_language, ConfigCSV.csv_path)

    base_path = "/media/raul/d1964fe0-512e-4389-b8f7-b1bd04e829612/Projects/Jobs/Word_Games/Arcane/ARCANE/Assets/src/config/Languages/Data/"

    characters = get_characters_from_laguage_json(
        language_iso=iso,
        path=base_path + "EntitiesLanguageJson.json",
        base_characters=characters,
        simple=False,
    )
    characters = get_characters_from_laguage_json(
        language_iso=iso,
        path=base_path + "EventsLanguageJson.json",
        base_characters=characters,
        simple=False,
    )

    characters = get_characters_from_laguage_json(
        language_iso=iso,
        path=base_path + "EventEffectsLanguageJson.json",
        base_characters=characters,
        simple=False,
    )
    characters = get_characters_from_laguage_json(
        language_iso=iso,
        path=base_path + "StaticTexts.json",
        base_characters=characters,
        simple=True,
    )
    print(characters)


def all_language_json():
    generate_all_json_to_language("Ingles", "en")
    generate_all_json_to_language("Espannol de Espanna", "es_es")
    generate_all_json_to_language("Espannol de latinoamerica", "es_lt")
    generate_all_json_to_language("Frances", "fr")
    generate_all_json_to_language("italiano", "it")
    generate_all_json_to_language("Aleman", "de")
    generate_all_json_to_language("Portugues", "pt")
    generate_all_json_to_language("ruso", "rs")
    generate_all_json_to_language("japones", "jp")
    generate_all_json_to_language("Chino Simplificado", "zh")
    generate_all_json_to_language("Koreano", "ko")

def generat_all_csv_languages():
    generate_csv_column_language("Ingles", ConfigCSV.csv_path)
    generate_csv_column_language("Espannol de Espanna", ConfigCSV.csv_path)
    generate_csv_column_language("Espannol de latinoamerica", ConfigCSV.csv_path)
    generate_csv_column_language("Frances", ConfigCSV.csv_path)
    generate_csv_column_language("italiano", ConfigCSV.csv_path)
    generate_csv_column_language("Aleman", ConfigCSV.csv_path)
    generate_csv_column_language("Portugues", ConfigCSV.csv_path)
    generate_csv_column_language("ruso", ConfigCSV.csv_path)
    generate_csv_column_language("japones", ConfigCSV.csv_path)
    generate_csv_column_language("Chino Simplificado", ConfigCSV.csv_path)
    generate_csv_column_language("Koreano", ConfigCSV.csv_path)

clear_console()
all_language_json()
# generat_all_csv_languages()
# get_characters("Japanese(ja)", "jp")
