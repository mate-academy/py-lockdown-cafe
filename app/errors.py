class VaccineError(Exception):
    """Exception if visitor doesn't have a vaccine"""


class NotVaccinatedError(VaccineError):
    """Exception if visitor doesn't have a vaccine key"""


class OutdatedVaccineError(VaccineError):
    """Exception if the vaccine is expired"""


class NotWearingMaskError(Exception):
    """Exception if visitor doesn't wear a mask"""
