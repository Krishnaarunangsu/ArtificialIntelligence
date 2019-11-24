# Python program showing abstract base class work
from abc import ABC, abstractmethod


class FileReader(ABC):
    """
    Abstract class for any file reader that is valid for Dataframe generation
    """
    @abstractmethod
    def import_data(self):
        pass
