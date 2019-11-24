import pandas as pd
import numpy as np


class LocSlicer:
    """
    class for Understanding Loc Slicing
    """

    @staticmethod
    def perform_loc_slicing(data, index=None, columns=None):
        """

        Args:
            data:
            index:
            columns:

        Returns:

        """
        df_1 = pd.DataFrame(data, index, columns)
        print(f'Snake Dataframe=\n{df_1}')
        print('*********************************************************************')
        print(f'Speed Details = \n{df_1["max_speed"]}')
        print('*********************************************************************')
        print(f'Speed Details of the Viper = {df_1["max_speed"]["viper"]}')
        print('#####################################USING loc##########################')
        print(f'Speed Details of the Viper = {df_1.loc["viper", "max_speed"]}')
        print('*********************************************************************')
        print(f'----------------------------------------------------------------------')
        print('Single label. Note this returns the row as a Series.')
        print(f'----------------------------------------------------------------------')
        print(f'Get Complete Viper Details at a shot = \n{df_1.loc["viper"]}')
        print(f'----------------------------------------------------------------------')
        print('List of labels. Note using [[]] returns a DataFrame.')
        print(f'----------------------------------------------------------------------')
        print(f'Get Complete Details of Viper & Sidewinder = \n{df_1.loc[["viper", "sidewinder"]]}')
        print('**************************************************************************')
        print(f'----------------------------------------------------------------------')
        print(f'Single label for row and column = {df_1.loc["viper", "shield"]}')
        print('**************************************************************************')
        print(f'----------------------------------------------------------------------')
        print(f'Get the details of a column for all the selected row labels =\
         \n{df_1.loc["cobra":"viper", "max_speed"]}')
        print('**************************************************************************')
        print('Suppressing some rows/labels')
        print(f'----------------------------------------------------------------------')
        print(f'Boolean list with the same length as the row axis =\
         \n{df_1.loc[[False, False, True]]}')
        print('**************************************************************************')
        print('Conditional that returns a boolean Series')
        print(df_1['shield'] > 5)
        print(f'----------------------------------------------------------------------')
        print(df_1.loc[df_1['shield'] > 5])
        print(f'-------------------------------shield==5---------------------------------------')
        print(df_1['shield'] == 5)
        print(f'-----------------------------------max_speed==5-----------------------------------')
        print(df_1['max_speed'] == 5)
        print(df_1.loc[df_1['max_speed'] == 5])
        print('**************************************************************************')
        print('Set value for all items matching the list of labels')
        df_1.loc[['viper', 'sidewinder'], ['shield']] = 50
        print(df_1)
        print('**************************************************************************')
        print('Set value for an entire row')
        df_1.loc['cobra'] = 10
        print(df_1)
        print('**************************************************************************')
        print('Set value for an entire column')
        df_1.loc[:, 'max_speed'] = 30
        print(df_1)
        print('**************************************************************************')
        print('Set value for rows matching callable condition')
        print(df_1['shield'] > 35)
        print('---------------------------------------------')
        print(df_1.loc[df_1['shield'] > 35])




        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html


    # Creating a 2 dimensional numpy array
    @staticmethod
    def build_2d_numpy_array(data_1, data_2, data_3):
        """

        Args:
            data_1:
            data_2:
            data_3:

        Returns:
            numpy_data

        """
        numpy_data = np.array([data_1, data_2, data_3])
        print(f'Numpy Array=\n{numpy_data}')
        return numpy_data


if __name__ == "__main__":
    loc_b = LocSlicer()
    data_1_list: list = [1, 2]
    data_2_list: list = [3, 4]
    data_3_list: list = [5, 6]
    numpy_ndarray = loc_b.build_2d_numpy_array(data_1_list, data_2_list, data_3_list)
    index = ['cobra', 'viper', 'sidewinder']
    columns = ['max_speed', 'shield']
    loc_b.perform_loc_slicing(numpy_ndarray, index, columns)
