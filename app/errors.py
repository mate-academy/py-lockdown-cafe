class VaccineError(Exception):
    def __init__(self, message: str = "Default VaccineError message") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Default VaccineError message") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Default VaccineError message") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Default VaccineError message") -> None:
        super().__init__(message)
