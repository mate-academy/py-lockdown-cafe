
class VaccineError(Exception):
    """Error related to vaccination"""


class NotVaccinatedError(VaccineError):
    """Error that person is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Error that person has outdated vaccine"""


class NotWearingMaskError(Exception):
    """Error that person without mask"""
