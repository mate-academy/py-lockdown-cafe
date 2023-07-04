class NotWearingMaskError(Exception):
    """This exception will be raised when a visitor doesn't wear a mask"""


class VaccineError(Exception):
    """Parent class for NotVaccinatedError and OutdatedVaccineError.
    This exception will be raised when there is issue with vaccination"""


class NotVaccinatedError(VaccineError):
    """This exception will be raised when there is no vaccination"""


class OutdatedVaccineError(VaccineError):
    """This exception will be raised when a vaccination is outdated"""
