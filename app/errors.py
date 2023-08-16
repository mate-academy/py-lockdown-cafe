class VaccineError(Exception):
    pass


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Not wearing a mask") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Outdated vaccine") -> None:
        super().__init__(message)
