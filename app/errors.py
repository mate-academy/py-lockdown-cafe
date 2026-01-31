class VaccineError(Exception):
    """This is paren class exception"""


class NotVaccinatedError(VaccineError):
    """This exception used when someone doesn't have vaccine"""


class OutdatedVaccineError(VaccineError):
    """This exception used when vaccine is out of date"""


class NotWearingMaskError(Exception):
    """This exception used when visitor not wearing mask"""
