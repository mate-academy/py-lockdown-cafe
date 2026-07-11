class VaccineError(Exception):
    """Some problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """Don't have vaccine"""


class OutdatedVaccineError(VaccineError):
    """The vaccine date expired"""


class NotWearingMaskError(Exception):
    """Don't wear mask"""
