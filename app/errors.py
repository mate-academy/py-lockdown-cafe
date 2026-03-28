class VaccineError(Exception):
    """Base exception for vaccine-related issues."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
