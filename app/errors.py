class VaccineError(Exception):
    """problems with the vaccine"""


class NotVaccinatedError(VaccineError):
    """If there is no vaccine"""


class OutdatedVaccineError(VaccineError):
    """The vaccination period is over"""


class NotWearingMaskError(Exception):
    """Visitor without a mask"""
