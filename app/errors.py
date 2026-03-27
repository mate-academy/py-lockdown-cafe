class VaccineError(Exception):
    """Vaccine problem"""


class NotVaccinatedError(VaccineError):
    """Visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Visitor's vaccine is expired"""


class NotWearingMaskError(Exception):
    """Visitor must wear mask"""
