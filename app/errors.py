class VaccineError(Exception):
    """Something wrong with vaccine"""


class NotVaccinatedError(VaccineError):
    """Vaccine is absent"""


class OutdatedVaccineError(VaccineError):
    """Vaccine is outdated"""


class NotWearingMaskError(Exception):
    """No mask on face"""
