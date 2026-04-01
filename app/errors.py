class VaccineError(Exception):
    def __init__(self, message="There is a vaccine-related issue.") -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    def __init__(self, message="The visitor is not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    def __init__(self, message="The visitor's vaccine is outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    def __init__(self, message="The visitor is not wearing a mask.") -> None:
        super().__init__(message)
