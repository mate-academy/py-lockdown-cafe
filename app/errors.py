class VaccineError(Exception):
    """Parent class for NotVaccinatedError
    and OutdatedVaccineError errors."""


class NotVaccinatedError(VaccineError):
    """Exception if the visitor does not have a vaccine"""


class OutdatedVaccineError(VaccineError):
    """Exception if the vaccine has expired"""


class NotWearingMaskError(Exception):
    """Exception if the visitor is not wearing a mask"""
