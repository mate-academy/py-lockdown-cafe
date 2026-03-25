class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has no vaccine key."""


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
