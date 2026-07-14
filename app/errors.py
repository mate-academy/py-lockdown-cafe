class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is missing a vaccine record."""


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine has expired."""


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
