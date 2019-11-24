# Series:
# Series is one dimensional(1-D) array defined in pandas that can be used to store any data type.
# a = pd.Series(Data, index = Index)
# Here, Data can be:
# 1)A Scalar value which can be integerValue, string
# 2)A Python Dictionary which can be Key, Value pair
# 3)A Ndarray
# Note: Index by default is from 0, 1, 2, …(n-1) where n is length of data.


import pandas as pd
from src.exception_handling.custom_exception_handling import IndexDataLengthNotMatching


class SeriesBuilding:
    """
    Class for Series Building
    """
    @staticmethod
    def get_data_series(data, index=None):
        """

        Args:
            data:list(int)
            index:int

        Returns:

        """
        data_series = pd.Series(data, index)
        print(f'Scalar Data Series = \n{data_series}')


def main():
    """

    Returns:

    """
    series_building = SeriesBuilding()
    scalar_data = [1, 2, 5, 7, 9, 6]
    data_index = [0, 1, 2, 3, 4, 5]
    if len(data_index) != len(scalar_data):
        raise IndexDataLengthNotMatching('Index Length & Data Length not matching')

    series_building.get_data_series(scalar_data, data_index)
    # series_building.data_series(scalar_data)

    dictionary: dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    series_building.get_data_series(dictionary)

    data_array = [[2, 3, 4], [5, 6, 7]]
    series_building.get_data_series(data_array)


if __name__ == "__main__":
    main()
