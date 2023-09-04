class VaccineError(Exception):
    """Parent class for errors"""


class NotVaccinatedError(VaccineError):
    """this error call when a visitor does not have a vaccine """


class OutdatedVaccineError(VaccineError):
    """this error call when a vaccine expired"""


class NotWearingMaskError(Exception):
    """this error call when visitor doesn't have a mask"""
