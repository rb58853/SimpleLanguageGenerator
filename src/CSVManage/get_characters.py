import pandas as pd


def get_characters_from_language(language, path, extra_container=[]):
    """Obtiene todos los caracteres que se usan en un idioma en el CSV"""
    csv = pd.read_csv(path)
    lines = csv.values.tolist()
    colums: list = csv.columns.to_list()
    index = colums.index(language)
    words_list = [str(value[index]) for value in lines]

    characters = []
    for value in words_list:
        for char in value:
            if char not in characters and char not in extra_container:
                characters.append(char)
    return "".join(characters)
