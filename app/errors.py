class VaccineError(Exception):
    """Base exception for vaccine-related entry errors."""


class NotVaccinatedError(VaccineError):
    """Raised when the visitor has no vaccine record."""


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine has expired."""


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
