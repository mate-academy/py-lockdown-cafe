class VaccineError(Exception):
    """Base class for all exceptions related to vaccination."""


class NotVaccinatedError(VaccineError):
    """This exception will be raised if visitor isn't vaccinated"""


class OutdatedVaccineError(VaccineError):
    """This exception will be raised if the vaccine is outdated"""


class NotWearingMaskError(Exception):
    """This exception will be raised if visitor isn't wearing the mask"""
