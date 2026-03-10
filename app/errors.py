class VaccineError(Exception):
    """Base exception for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when visitor has no vaccine key."""


class OutdatedVaccineError(VaccineError):
    """Raised when visitor's vaccine has expired."""


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
