class VaccineError(Exception):
    pass


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Visitor vaccine is outdated!") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Visitor is not vaccinated!") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Not have a mask") -> None:
        super().__init__(message)
