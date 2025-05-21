class VaccineError(Exception):
    """Base exception for vaccine errors"""


class NotVaccinatedError(VaccineError):
    """Exception means that visitor is not vaccinated"""


class OutdatedVaccineError(VaccineError):
    """Exception means that visitor's vaccine is expired"""


class NotWearingMaskError(Exception):
    """Exception, if visitor isn't wearing a mask"""
