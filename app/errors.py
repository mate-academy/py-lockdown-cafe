"""
Exception module for validating health protocols.
"""


class VaccineError(Exception):
    """
    Exception for troubles with vaccinations.
    """
    pass


class NotVaccinatedError(VaccineError):
    """
    Exception for visitors without vaccination records.
    """
    pass


class OutdatedVaccineError(VaccineError):
    """
    Exception for visitors with expired vaccinations.
    """
    pass


class NotWearingMaskError(Exception):
    """
    Exception for visitors not wearing masks.
    """
    pass
