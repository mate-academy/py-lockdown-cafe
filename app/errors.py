class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            message: str = "All friends should be vaccinated"
    ) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(
            self,
            message: str = "Friends should buy masks"
    ) -> None:
        super().__init__(message)
