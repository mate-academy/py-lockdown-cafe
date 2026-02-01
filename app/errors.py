class VaccineError(Exception):
    """Base Vaccine Error"""


class NotVaccinatedError(VaccineError):
    """No Vaccinated visitor"""


class OutdatedVaccineError(VaccineError):
    """Outdated Vaccine"""


class NotWearingMaskError(Exception):
    """Not Wearing Mask"""
