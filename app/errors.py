

class VaccineError(Exception):
    """Vaccine Error"""


class NotVaccinatedError(VaccineError):
    """Not Vaccine Error"""


class OutdatedVaccineError(VaccineError):
    """Outdated Vaccine Error"""


class NotWearingMaskError(Exception):
    """Not Wearing Mask Error"""
