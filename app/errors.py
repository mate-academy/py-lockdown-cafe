"""
This module holds possible errors
"""


class NotWearingMaskError(Exception):
    """
    Everyone has to wear masks in order to enter the premises
    """
    pass


class VaccineError(Exception):
    """
    Just a parent
    """
    pass


class NotVaccinatedError(VaccineError):
    """
    Everyone has to be vaccinated to enter the premises
    """
    pass


class OutdatedVaccineError(VaccineError):
    """
    Every vaccination has to be up-to-date
    """
    pass
