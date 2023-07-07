class VaccineError(Exception):
    """Parent class for vaccine errors"""


class NotVaccinatedError(VaccineError):
    """Error not vaccinated visitor"""


class OutdatedVaccineError(VaccineError):
    """Error expired date of vaccine"""


class NotWearingMaskError(Exception):
    """Mask availability error"""
