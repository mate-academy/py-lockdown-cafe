class VaccineError(Exception):
    """Base class for exceptions related to vaccination."""


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine is expired."""


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
