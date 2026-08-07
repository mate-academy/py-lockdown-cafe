class VaccineError(Exception):
    """Base exception for all vaccine-related problems."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has no vaccine information."""


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine has expired."""


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
