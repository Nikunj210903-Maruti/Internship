from builtins import Exception


class ThaweMarineServiceException(Exception):
    pass


class InvalidEmailData(ThaweMarineServiceException):
    pass
