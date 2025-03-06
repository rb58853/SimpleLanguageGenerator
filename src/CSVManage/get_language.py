from src.OpenAI.gpt_service import GPT
from src.Config.config import ConfigCSV
import pandas as pd

gpt: GPT = GPT()


def generate_csv_column_language(language: str, path: str) -> None:
    """
    Crea una columna de CVS con un nuevo lenguaje. Lo hace sobre el archivo que se encuentra en la direccion `path`
    """
    print(f"\n{language}")
    csv = pd.read_csv(path)
    lines = [line for line in csv.values]
    lines = [
        [
            value.replace('"', '""') if (isinstance(value, str)) else str(value)
            for value in line
        ]
        for line in lines
    ]
    # Esto extrar la primera lista de terminos. xq values[0] son los del csv y values [1] son los id del string
    strings_list = [value[2] for value in lines]

    strings_list = [str(value) for value in strings_list]

    current = csv.columns.to_list()
    current = [[f'"{value}"' for value in current]]
    current += [
        [f'"{value}"' if (isinstance(value, str)) else str(value) for value in line]
        for line in lines
    ]
    end = [f"{language}"]
    index = 0
    while len(strings_list) > index:
        gpt_list = gpt.strings_list_to_laguage(
            language, strings_list[index : index + ConfigCSV.batch_size]
        )
        end += gpt_list
        print(f"{index}:{index+ConfigCSV.batch_size} -> {len(gpt_list)}")
        index += ConfigCSV.batch_size

    end = [
        value.replace('"', '""').replace('""""', '""') if isinstance(value, str) else ""
        for value in end
    ]
    end = [f'"{value}"' if isinstance(value, str) else "" for value in end]

    if len(strings_list) + 1 == len(end):
        current = [
            current_value + [end_value]
            for current_value, end_value in zip(current, end)
        ]
        final = "\n".join([",".join(line) for line in current])
        with open(path, "w") as archivo:
            archivo.write(final)
    else:
        print("No se convirtieron todos los textos")
