class VaccineError(Exception):
    """General class for vaccine-related errors"""


class NotVaccinatedError(VaccineError):
    """The visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The visitor has an overdue vaccine"""


class NotWearingMaskError(Exception):
    """The visitor does not have a mask"""
