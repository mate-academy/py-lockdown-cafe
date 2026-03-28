class VaccineError (Exception):
    def __init__(self, message: str = "Vaccine error") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Not Vaccinated Error") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Outdated Vaccine Error") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(
            self,
            message: str = "The visitor is not wearing a mask"
    ) -> None:
        super().__init__(message)
