class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor has an expired vaccine."""


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
