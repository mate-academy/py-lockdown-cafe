class VaccineError(Exception):
    """This class is created to combine vaccine exceptions"""


class NotVaccinatedError(VaccineError):
    """This exception will be raised in case the visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """This exception will be raised in case the visitor vaccine is outdated"""


class NotWearingMaskError(Exception):
    """This exception will be raised in case the visitor is not wearing mask"""
