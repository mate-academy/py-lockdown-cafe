class VaccineError(Exception):
    """All errors with vaccine"""


class NotVaccinatedError(VaccineError):
    """If the visitor does not have a vaccine key"""


class OutdatedVaccineError(VaccineError):
    """if the vaccine has expired"""


class NotWearingMaskError(Exception):
    """if visitors are not wearing masks"""
