class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Visitor should have a vaccine"""


class OutdatedVaccineError(VaccineError):
    """The vaccine must not be expired"""


class NotWearingMaskError(Exception):
    """all visitors must wear masks"""
