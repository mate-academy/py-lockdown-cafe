class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "NotVaccinatedError") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "OutdatedVaccineError") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "NotWearingMaskError") -> None:
        super().__init__(message)
