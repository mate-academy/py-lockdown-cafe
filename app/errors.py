class VaccineError(Exception):
    def __init__(self, message: str = "Vaccine error occurred") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message: str = "The visitor is not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message: str = "Visitors vaccination is outdated"
                 ) -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message: str = "Visitor not wearing a mask"
                 ) -> None:
        super().__init__(message)
