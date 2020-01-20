from abc import ABC, abstractmethod


class ExtractDataFromFileService(ABC):

    @abstractmethod
    def extract_data_from_file(self):
        pass
