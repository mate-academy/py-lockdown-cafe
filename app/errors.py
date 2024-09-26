class VaccineError(Exception):
    """Error"""


class NotVaccinatedError(VaccineError):
    """Error"""


class OutdatedVaccineError(VaccineError):
    """Error"""


class NotWearingMaskError(Exception):
    """Error"""
