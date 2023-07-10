class VaccineError(Exception):
    """Parent error"""


class NotVaccinatedError(VaccineError):
    """This error return when visitor doesn't have vaccine"""


class OutdatedVaccineError(VaccineError):
    """This error return when expiration date doesn't have a normal date"""


class NotWearingMaskError(Exception):
    """The visitor don't have a mask"""
