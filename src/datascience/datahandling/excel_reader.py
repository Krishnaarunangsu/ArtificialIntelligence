#  Implementing class of FileReader
from abc import ABC
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import ExcelWriter
from pandas import ExcelFile

from src.datascience.datahandling.file_reader import FileReader


class ExcelReader(FileReader, ABC):
    """
        class for specific implementation of reading a excel file
    """

    def __init__(self, excel_file):
        """

        Args:
            excel_file:
        """
        self.excel_file = excel_file

    def import_data(self) -> object:
        """
        Import excel data
        Returns: dataframe_excel

        """
        dataframe_excel = pd.read_excel(self.excel_file, sheet_name='Sheet1')
        return dataframe_excel

    @staticmethod
    def understand_data(data_frame):
        """

        Args:
            data_frame:

        Returns:

        """
        print(f'DataFrame:\n{data_frame.describe()}')
        print(f'Top three:\n{data_frame.head(3)}')
        print(f'Columns:\n{data_frame.columns}')  # show the features and label
        print(f'Shape:{data_frame.shape}')  # instances vs features + label (8, 5)

        sns.set(font_scale=1.5)
        countplt = sns.countplot(x='Species', data=data_frame, palette='hls')
        plt.show()


