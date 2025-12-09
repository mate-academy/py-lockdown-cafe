class VaccineError(Exception):
    """Parent class for vaccine-related errors"""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when visitor is not vaccinated"""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when visitor's vaccine is expired"""
    pass


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask"""
    pass
