class VaccineError(Exception):
    def __init__(self, message: str = "VaccineError") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __str__(self) -> str:
        return "NotVaccinatedError"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError"


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "NotWearingMaskError") -> None:
        super().__init__(message)
