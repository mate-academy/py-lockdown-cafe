class VaccineError(Exception):
    """Error occur if visitor has problem with vaccine"""


class NotVaccinatedError(VaccineError):
    """Error occur if visitor doesn't have vaccine"""


class OutdatedVaccineError(VaccineError):
    """Error occur if vaccine has been expired"""


class NotWearingMaskError(Exception):
    """Error occur if visitor doesn't wear a mask"""
