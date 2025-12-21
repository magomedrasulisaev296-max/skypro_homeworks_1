import pandas as pd


def read_csv_file(road_to_csv_file: str) -> dict:
    """возврощает csv файлы в ввиде словоря"""
    df = pd.read_csv(road_to_csv_file)
    return df.to_dict(orient="records")


def read_excel_file(road_to_excel_file: str):
    """возврощает excel файлы в ввиде словоря"""
    df = pd.read_excel(road_to_excel_file)
    return df.to_dict(orient="records")
