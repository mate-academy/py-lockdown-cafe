class VaccineError(Exception):
    """Base class for exceptions in this module."""


class OutdatedVaccineError(VaccineError):
    """Raised when a vaccine is outdated"""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated"""


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask"""
