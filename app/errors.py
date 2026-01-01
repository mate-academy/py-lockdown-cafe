class VaccineError(Exception):
    """Visitor have a problem with a vaccine"""


class NotVaccinatedError(VaccineError):
    """"Visitor doesn't have a vaccine"""


class OutdatedVaccineError(VaccineError):
    """Visitor have expired vaccine"""


class NotWearingMaskError(Exception):
    """Visitor doesn't have mask"""
