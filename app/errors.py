class VaccineError(Exception):
    """All issues with vaccine"""


class NotVaccinatedError(VaccineError):
    """Occurs when visitor does not have a vaccine key"""


class OutdatedVaccineError(VaccineError):
    """Occurs when visitor's vaccine is expired"""


class NotWearingMaskError(Exception):
    """Occurs when visitor does not have a mask"""
