class VaccineError(Exception):

    def __init__(self, message: str) -> None:  # Додана анотація типу
        super().__init__(message)


class NotVaccinatedError(VaccineError):

    def __init__(self, message: str) -> None:  # Додана анотація типу
        super().__init__(message)


class OutdatedVaccineError(VaccineError):

    def __init__(self, message: str) -> None:  # Додана анотація типу
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str) -> None:  # Додана анотація типу
        super().__init__(message)
