class VaccineError(Exception):
    """Base class for vaccine-related errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    """Raised when visitor has no vaccine."""


class OutdatedVaccineError(VaccineError):
    """Raised when visitor's vaccine is expired."""


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
