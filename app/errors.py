class VaccineError(Exception):
    """Exception, which will be raised, if visitor don't have valid vaccine"""


class NotVaccinatedError(VaccineError):
    """Exception if visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Exception if vaccine is expired"""


class NotWearingMaskError(Exception):
    """Exception if visitor is not wearing a masks"""
