class NotWearingMaskError(Exception):
    """Base class"""
    pass


class VaccineError(Exception):
    """Exception raised when there are issues with visitor's vaccine"""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated"""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception is raised when visitor's vaccine is expired"""
    pass
