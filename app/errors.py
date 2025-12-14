class VaccineError(Exception):
    """Parental class to check the vaccine"""


class NotVaccinatedError(VaccineError):
    """Checking whether the vaccination is overdue"""


class OutdatedVaccineError(VaccineError):
    """Checking whether the visitor is vaccinated"""


class NotWearingMaskError(Exception):
    """Checking the presence of a mask"""
