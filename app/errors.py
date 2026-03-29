class VaccineError(Exception):
    """Parent class"""


class NotWearingMaskError(Exception):
    """All visitors must wear masks"""


class NotVaccinatedError(VaccineError):
    """Visitor does not have a vaccine."""


class OutdatedVaccineError(VaccineError):
    """The vaccine must not be expired"""
