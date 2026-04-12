class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when visitor has no vaccine."""

    def __init__(self, message: str = "Visitor is not vaccinated.") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when vaccine is expired."""

    def __init__(self,
                 message: str = "Visitor's vaccine is outdated.") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""

    def __init__(self,
                 message: str = "Visitor is not wearing a mask.") -> None:
        super().__init__(message)
