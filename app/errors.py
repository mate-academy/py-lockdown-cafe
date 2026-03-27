class VaccineError(Exception):
    """Base class for all vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor does not have a vaccine record."""
    def __init__(self, message: str = "Visitor is not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is outdated."""
    def __init__(self, message: str = "Vaccine is outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    def __init__(self, message: str = "Visitor is not wearing a mask.") -> None:
        super().__init__(message)


