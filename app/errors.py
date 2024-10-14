class VaccineError(Exception):
    """Person has problems with the vaccine"""


class NotVaccinatedError(VaccineError):
    """Person doesn't have a vaccine"""


class OutdatedVaccineError(VaccineError):
    """The expiration date was expired"""


class NotWearingMaskError(Exception):
    """Person doesn't have the mask"""
