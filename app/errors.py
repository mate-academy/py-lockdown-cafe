class VaccineError(Exception):
    """Raises if sth is with vaccination"""


class NotVaccinatedError(VaccineError):
    """Raises if visitor is nor vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Raises if vaccine is outdated"""


class NotWearingMaskError(Exception):
    """Raises if visitor is without a mask"""
