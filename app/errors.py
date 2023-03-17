class VaccineError(Exception):
    """Raise when visitor doesn't have valid vaccine"""


class NotVaccinatedError(VaccineError):
    """Raise when visitor doesn't have any vaccine"""


class OutdatedVaccineError(VaccineError):
    """Raise when visitor have an outdated vaccine"""


class NotWearingMaskError(Exception):
    """Raise when visitor doesn't have a mask"""
