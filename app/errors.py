class VaccineError(Exception):
    """VaccineError exception"""


class NotVaccinatedError(VaccineError):
    """Vaccination check"""


class OutdatedVaccineError(VaccineError):
    """Vaccination expiration date check"""


class NotWearingMaskError(Exception):
    """Mask check"""
