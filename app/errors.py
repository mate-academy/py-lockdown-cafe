
class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Call when visitor without vaccine"""


class OutdatedVaccineError(VaccineError):
    """Call when date of vaccination passed"""


class NotWearingMaskError(Exception):
    """Call when a visitor without a mask"""
