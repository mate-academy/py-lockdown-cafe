"""
This module holds possible errors
"""


class NotWearingMaskError(Exception):
    """
    No mask -> virus gets in -> die
    """
    pass


class VaccineError(Exception):
    """
    Just a parent
    """
    pass


class NotVaccinatedError(VaccineError):
    """
    No vaccine -> virus gets in -> die
    """
    pass


class OutdatedVaccineError(VaccineError):
    """
    Outdated vaccine -> virus gets in -> die
    """
    pass
