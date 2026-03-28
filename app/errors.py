class VaccineError(Exception):
    """ERROR"""


class NotVaccinatedError(VaccineError):
    """ERROR"""


class OutdatedVaccineError(VaccineError):
    """ERROR"""


class NotWearingMaskError(Exception):
    """ERROR"""
