class VaccineError(Exception):
    """Exception raised when the problem is related to vaccine"""


class NotVaccinatedError(VaccineError):
    """Exception raised if not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Exception raised if outdated vaccine"""


class NotWearingMaskError(Exception):
    """Exception raised if not wearing a mask"""
