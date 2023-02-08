class VaccineError(Exception):
    """Common class for vaccination errors"""


class NotVaccinatedError(VaccineError):
    """Exception for not vaccinated visitor"""


class OutdatedVaccineError(VaccineError):
    """Exception for expired vaccine"""


class NotWearingMaskError(Exception):
    """Exception for visitor without mask"""
