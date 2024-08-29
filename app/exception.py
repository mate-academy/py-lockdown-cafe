class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    def __init__(
            self,
            message: str = "Visitor is not vaccinated. Access denied."
    ) -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(
            self,
            message: str = "Vaccine is outdated. Access denied."
    ) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(
            self,
            message: str = "Visitor is not wearing a mask. Access denied."
    ) -> None:
        super().__init__(message)
