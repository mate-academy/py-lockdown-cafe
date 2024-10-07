
class VaccineError(Exception):
    """Parent class for NotVaccinatedError and OutdatedVaccineError errors"""


class NotVaccinatedError(VaccineError):
    """The visitor does not have a vaccine key."""


class OutdatedVaccineError(VaccineError):
    """The vaccine must not be expired"""


class NotWearingMaskError(Exception):
    """All visitors must wear masks"""
