class VaccineError(Exception):
    """The visitor is not vaccinated"""


class NotVaccinatedError(VaccineError):
    """The visitor does not have a vaccine key"""


class OutdatedVaccineError(VaccineError):
    """The vaccine is expired"""


class NotWearingMaskError(Exception):
    """The visitor does not wear a mask"""
