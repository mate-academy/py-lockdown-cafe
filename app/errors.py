__all__ = [
    "VaccineError",
    "NotVaccinatedError",
    "OutdatedVaccineError",
    "NotWearingMaskError",
]


class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when visitor has no vaccine information."""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Visitor is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    """Raised when visitor's vaccine is expired."""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or "Visitor's vaccine is expired.")


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(
            message or "Mask is required to enter the cafe."
        )
