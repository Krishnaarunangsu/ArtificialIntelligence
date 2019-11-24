import pandas as pd
from src.datascience.datahandling.csv_reader import CSVReader
from src.datascience.datahandling.excel_reader import ExcelReader


if __name__ == "__main__":
    csv_reader = CSVReader('../../../data/movie_metadata.csv')
    dataframe_result: object = csv_reader.import_data()
    print(f'Original Content-Dataframe:\n{dataframe_result}')
    print('*********************************************************')
    csv_reader.understand_data(dataframe_result)

    # excel_reader = ExcelReader('../../../data/iris_subset.xlsx')
    # dataframe_result: object = excel_reader.import_data()
    # print(f'Dataframe:\n{dataframe_result}')
    # excel_reader.understand_data(dataframe_result)
