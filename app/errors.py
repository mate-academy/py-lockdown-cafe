class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when the visitor is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is outdated."""


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
