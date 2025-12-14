class VaccineError(Exception):
    """if the visitor does not have a problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """if the visitor does not have a vaccine key"""


class OutdatedVaccineError(VaccineError):
    """If the vaccine not expired"""


class NotWearingMaskError(Exception):
    """if the visitor does not have a mask"""
