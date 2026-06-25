class NotWearingMaskError(Exception):
    """This exception occurs when
     the visitor has no mask."""


class VaccineError(Exception):
    """This exception occurs when
     visitor has some problem with the vaccination"""


class NotVaccinatedError(VaccineError):
    """This exception occurs when
    the visitor has exactly no vaccine"""


class OutdatedVaccineError(VaccineError):
    """This exception occurs when
    the visitor has an outdated vaccine"""
