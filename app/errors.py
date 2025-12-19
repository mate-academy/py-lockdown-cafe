class VaccineError(Exception):
    """
    This exception will be raised if visitor does not have 'vaccine' key
    or vaccine has expired
    """


class NotVaccinatedError(VaccineError):
    """This exception will be raised if visitor does not have 'vaccine' key"""


class OutdatedVaccineError(VaccineError):
    """This exception will be raised if vaccine is expired"""


class NotWearingMaskError(Exception):
    """This exception will be raised if visitor is not wearing the mask"""
