class VaccineError(Exception):
    """Raising when there are any problems with vaccine"""


class NotVaccinatedError(VaccineError):
    """Raising when there is no vaccine"""


class OutdatedVaccineError(VaccineError):
    """Raising when vaccine is expired"""


class NotWearingMaskError(Exception):
    """Raising when there is no mask"""
