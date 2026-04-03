
class NotWearingMaskError(Exception):
    """Exception"""


class VaccineError(Exception):
    """Exception"""


class NotVaccinatedError(VaccineError):
    """Exception"""


class OutdatedVaccineError(VaccineError):
    """"Exception"""
