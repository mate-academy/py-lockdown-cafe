class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Client is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Customer has an expired vaccine"""


class NotWearingMaskError(Exception):
    """Customer does not wear a mask"""
