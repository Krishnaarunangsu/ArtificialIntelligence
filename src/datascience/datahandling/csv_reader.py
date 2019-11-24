#  Implementing class of FileReader
from abc import ABC
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.datascience.datahandling.file_reader import FileReader


class CSVReader(FileReader, ABC):
    """
     class for specific implementation of reading a csv file
    """

    def __init__(self, csv_file):
        """

        :param csv_file: file
        """
        self.csv_file = csv_file

    def import_data(self) -> object:
        """
        Import csv data
        :return dataframe_from_csv: dataframe
        """
        dataframe_from_csv = pd.read_csv(self.csv_file, sep=',')
        return dataframe_from_csv

    @staticmethod
    def understand_data(data_frame):
        """

        :param data_frame:
        :return:
        """
        print(f'DataFrame Information:\n{data_frame.dtypes}')
        print('*********************************************************')
        print(f'DataFrame Exploration:\n{data_frame.describe()}')
        print('*********************************************************')
        print(f'Top three:\n{data_frame.head(3)}')
        print('*********************************************************')
        print(f'Columns:\n{data_frame.columns}')  # show the features and label
        print('*********************************************************')
        column_list: list = list(data_frame.columns.values)
        print(f'Column Names:\n{list(data_frame.columns.values)}')  # show the features and label
        print('*********************************************************')
        print(f'Shape:{data_frame.shape}')  # instances vs features + label (4521, 17)
        for idx, column_name in enumerate(column_list):
            print(f'column_list[{idx}]->{column_name}')

        # sns.set(font_scale=1.5)
        # countplt = sns.countplot(x='y', data=data_frame, palette='hls')
        # plt.show()
