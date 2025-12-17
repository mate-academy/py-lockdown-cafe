class VaccineError(Exception):
    """This exception will be raised if there are problems with vaccine"""


class NotVaccinatedError(VaccineError):
    """This exception will be raised if somebody doesn't have a vaccine"""


class OutdatedVaccineError(VaccineError):
    """This exception will be raised if vaccinated certificate is expired"""


class NotWearingMaskError(Exception):
    """This exception will be raised if somebody isn't wearing a mask"""
