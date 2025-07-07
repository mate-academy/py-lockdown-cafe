class VaccineError(Exception):
    """Problem with the vaccine"""


class NotVaccinatedError(VaccineError):
    """Visitor is without a vaccine"""


class OutdatedVaccineError(VaccineError):
    """Vaccine is expired"""


class NotWearingMaskError(Exception):
    """Visitor is without a mask"""
