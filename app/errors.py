class VaccineError(Exception):
    """Base exception for all vaccine-related problems"""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has vo vaccine information at all"""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine has already expired"""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask"""
    pass
