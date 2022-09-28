class VaccineError(Exception):
    """problems with the vaccine"""


class NotWearingMaskError(Exception):
    """the guest without mask"""


class NotVaccinatedError(VaccineError):
    """the guest without vaccine"""


class OutdatedVaccineError(VaccineError):
    """the vaccine is outdated"""
