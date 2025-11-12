class VaccineError(Exception):
    """Vaccine error class"""


class NotVaccinatedError(VaccineError):
    """Not Vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Outdated Vaccine"""


class NotWearingMaskError(Exception):
    """Not Wearing Mask"""
