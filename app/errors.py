class VaccineError(Exception):
    """main error class"""


class NotVaccinatedError(VaccineError):
    """to check if visitor have a vaccine"""


class OutdatedVaccineError(VaccineError):
    """to check valid data of vaccine"""


class NotWearingMaskError(Exception):
    """to check if wearing the mask"""
