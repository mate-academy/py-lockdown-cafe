class VaccineError(Exception):
    """Base class for all vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is outdated."""


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
