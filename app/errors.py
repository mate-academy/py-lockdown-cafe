class VaccineError(Exception):
    def __init__(
            self,
            message: str = "Something is wrong with your vaccine"
    ) -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "Not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            message: str = "An expired vaccine date"
    ) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Not wearing a mask") -> None:
        super().__init__(message)
