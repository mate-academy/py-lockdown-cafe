class NotWearingMaskError(Exception):
    """The visitor does not wear a mask"""


class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """The visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """The vaccine is expired"""
