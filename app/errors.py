class VaccineError(Exception):
    """Custom exception for errors raised by Vaccine"""


class NotVaccinatedError(VaccineError):
    """Not Vaccinated Error"""


class OutdatedVaccineError(VaccineError):
    """Outdated Vaccine Error"""


class NotWearingMaskError(Exception):
    """Not Wearing Mask Error"""
