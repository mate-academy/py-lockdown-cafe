class NotWearingMaskError(Exception):
    """Checking whether the visitor has a mask"""


class VaccineError(Exception):
    """Checking troubles with vaccine"""


class NotVaccinatedError(VaccineError):
    """Checking visitor is vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Checking whether the vaccination period has not expired"""
