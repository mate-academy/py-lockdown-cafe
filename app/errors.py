class VaccineError(Exception):
    def __init__(self, message: str = "") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor should to buy a mask!") -> None:
        super().__init__(message)
