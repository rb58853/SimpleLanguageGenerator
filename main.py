from src.CSVManage.get_language import generate_csv_column_language
from src.Config.config import ConfigCSV

def generate_language_csv_column(language: str) -> None:
    csv_path: str = ConfigCSV.csv_path
    generate_csv_column_language(language=language, path=csv_path)
