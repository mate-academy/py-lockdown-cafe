class VaccineError(Exception):
    """Parent vaccine error"""


class NotVaccinatedError(VaccineError):
    """Exception if a visitor don't have the vaccine"""


class OutdatedVaccineError(VaccineError):
    """Exception if vaccine expired"""


class NotWearingMaskError(Exception):
    """Exception if a visitor don't have a mask"""
