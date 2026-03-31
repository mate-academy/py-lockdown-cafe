class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Visitor's vaccine is expired."""


class NotWearingMaskError(Exception):
    """Visitor is not wearing a mask"""
