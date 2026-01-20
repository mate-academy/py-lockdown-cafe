class VaccineError(Exception):
    """Base class for vaccine-related errors"""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when the visitor's is not wearing mask."""
    pass
