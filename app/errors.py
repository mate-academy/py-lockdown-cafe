"""Custom exception hierarchy for the Lockdown Cafe task."""


class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has no valid vaccination record."""

    def __init__(self, message: str = "Visitor is not vaccinated") -> None:
        super().__init__(message)


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""

    def __init__(self, message: str = "Vaccine is expired") -> None:
        super().__init__(message)


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""

    def __init__(self, message: str = "Mask is required") -> None:
        super().__init__(message)
#
