from abc import ABC, abstractmethod


class FilterEmailService(ABC):

    @abstractmethod
    def filter_email(self):
        pass
