class VaccineError(Exception):
    """Vaccine Error"""


class NotVaccinatedError(VaccineError):
    """Not Vaccinated Error"""


class OutdatedVaccineError(VaccineError):
    """Outdated Vaccine Error"""


class NotWearingMaskError(Exception):
    """Not Wearing Mask Error"""
