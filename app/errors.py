class VaccineError(Exception):
    """This error occurs when there're any vaccine errors"""


class NotVaccinatedError(VaccineError):
    """This error occurs when visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """This error occurs if visitor's vaccine is outdated"""


class NotWearingMaskError(Exception):
    """This error occurs if visitor is not wearing a mask"""
