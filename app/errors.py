class VaccineError(Exception):
    """Vaccine Error - parent class"""


class NotVaccinatedError(VaccineError):
    """Not Vaccinated Error - Vaccine Error child class"""


class OutdatedVaccineError(VaccineError):
    """Outdated Vaccine Error - Vaccine Error child class"""


class NotWearingMaskError(Exception):
    """Not Wearing Mask Error - Vaccine Error child class"""
