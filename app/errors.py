class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception for visitors who are not vaccinated."""

    def __init__(self, message: str = "Visitor is not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Exception for visitors with an expired vaccine."""

    def __init__(self, message: str = "Vaccine is outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Exception for visitors who are not wearing a mask."""

    def __init__(self, message: str = "Visitor is not wearing a mask.")\
            -> None:
        super().__init__(message)
