class VaccineError(Exception):
    """raised when the visitor has a problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """raised when the visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """raised when the visitors vaccine is outdated"""


class NotWearingMaskError(Exception):
    """raised when the visitor is not wearing mask"""
