class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "No vaccination") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "The vaccine expired") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Did not wear a mask") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message
