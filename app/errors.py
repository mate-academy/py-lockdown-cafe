class NotWearingMaskError(Exception):
    def __init__(
        self,
        message: str = "Visitor should wear a mask"
    ) -> None:
        super().__init__(message)


class VaccineError(Exception):
    def __init__(
        self,
        message: str = "All friends should be vaccinated"
    ) -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(
            self,
            message: str = "Visitor should be vaccinated"
    ) -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            message: str = "Vaccine has expired"
    ) -> None:
        super().__init__(message)
