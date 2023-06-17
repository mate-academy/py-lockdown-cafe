class VaccineError(Exception):
    """Visitor either is not vaccinated or his vaccine is expired"""


class NotVaccinatedError(VaccineError):
    """Visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The visitor's  vaccine is expired"""


class NotWearingMaskError(Exception):
    """Visitor must wear mask"""
