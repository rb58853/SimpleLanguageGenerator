from src.CSVManage.get_language import generate_csv_column_language
import pandas as pd


def generate_n_columns_from_languages_list(
    languages: list,
    path,
):
    """Por cada idioma pasado en la lista, crea una columna de CVS con un nuevo lenguaje. Lo hace sobre el archivo que se encuentra en la direccion `path`"""

    for lang in languages:
        generate_csv_column_language(
            lang,
            path,
        )


def delete_Kth_last_columns(k, path):
    """
    Elimina las ultimas K columnas del CVS
    """
    csv = pd.read_csv(path)
    lines = [line for line in csv.values]
    lines = [
        [
            value.replace('"', '""') if (isinstance(value, str)) else str(value)
            for value in line
        ]
        for line in lines
    ]
    current = csv.columns.to_list()[:-k]
    current = [[f'"{value}"' for value in current]]
    current += [
        [
            f'"{value}"' if (isinstance(value, str)) else str(value)
            for value in line[:-k]
        ]
        for line in lines
    ]

    final = "\n".join([",".join(line) for line in current])
    with open(path, "w") as archivo:
        archivo.write(final)
