class VaccineError(Exception):
    def __init__(self, message: str = "Vaccine error") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "You must be vaccinated!") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Your vaccine is outdated!") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "You should wear some mask!") -> None:
        super().__init__(message)
