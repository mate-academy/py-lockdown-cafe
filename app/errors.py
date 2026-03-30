class VaccineError(Exception):
    """if visiter has problems with the vaccine"""


class NotVaccinatedError(VaccineError):
    """"if visiter not vaccined, raise this error"""


class OutdatedVaccineError(VaccineError):
    """if vaccine is expired, raise this error"""


class NotWearingMaskError(Exception):
    """if visitor don't wear mask, raise this error"""
