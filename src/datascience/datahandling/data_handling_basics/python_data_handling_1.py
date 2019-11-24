import numpy as np


# Sorting


class SortData:
    """
    Class for Sorting Data
    """

    def __init__(self, data):
        """
        Initialization of the class instance variables
        Args:
            data:
        """
        self.data = data
        self.sorted_data = None

    def sort_data(self, sort_order: bool = False):
        """

            Args:
                sort_order:
                self:

            Returns:

        """
        self.sorted_data = sorted(self.data, reverse=sort_order)
        return self.sorted_data


class NumpyHelper:
    """

    """

    def __init__(self):
        """

        """

    def numpy_array_builder(self):
        """

        Returns:

        """
        numpy_array_1 = np.array([[4, 0, 5],
                                  [2, 8, 4]])

        print(numpy_array_1[0][0])

    def get_numpy_median(self, numpy_arr):
        """

        Args:
            numpy_arr:

        Returns:

        """
        median = np.median(numpy_arr)
        return median


def main():
    """
    Helper method main
    Returns:

    """
    data = [0, 5, 15, 5, 10, 8]
    sort_data_obj = SortData(data)
    result_sorted_data = sort_data_obj.sort_data()
    print(result_sorted_data)

    numpy_helper = NumpyHelper()
    numpy_helper.numpy_array_builder()

    numpy_array_2 = np.array([4.19, 3.65, 2.93])
    median_result = numpy_helper.get_numpy_median(numpy_array_2)
    print(median_result)

    costs = np.column_stack(([2, 1, 2, 1],
                             [4, 6, 5, 5]))
    print(costs)
    print(np.mean(costs[:, 0]))
    print(np.mean(costs[:, 1]))
    print(costs[1, :])
    print(np.mean(costs[1, :]))
    print(costs[0, :])
    print(np.mean(costs[0, :]))
    sum_total = [1, 0, 1] + [2, 4, 6]
    print(sum_total)
    y = [1, 3, 5, 11]
    z = y.reverse()
    print(z)
    foo = [0.2, 1.7, "A", "Wed", 1.5]
    foo[3:5] = ["E", "F"]
    print(foo)


if __name__ == "__main__":
    main()
    help(len)
