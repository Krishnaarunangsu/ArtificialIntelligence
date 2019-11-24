# DataFrames:
# DataFrames is two-dimensional(2-D) data structure defined in pandas which consists of rows and columns.
# Here, Data can be:
# 1) One or more dictionaries
# 2) One or more Series
# 3) 2D-numpy Ndarray


import pandas as pd


class DataFrameBuilder:
    """
    DataFrame Builder
    """
    @staticmethod
    def get_data_frame(data: object):
        """

        Args:
            data:

        Returns:

        """
        dataframe = pd.DataFrame(data)
        print(f'Dataframe=\n{dataframe}')


def main():
    """

    Returns:

    """
    # Program to create dataframe two dictionaries
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    dict2 = {'a': 5, 'b': 6, 'c': 7, 'd': 8, 'e': 9}
    dict_data: dict = {'first': dict1, 'second': dict2}
    df_builder = DataFrameBuilder()
    df_builder.get_data_frame(dict_data)


if __name__ == "__main__":
    main()
