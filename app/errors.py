class VaccineError(Exception):
    """Base class for exceptions related to vaccines."""
    pass

class NotVaccinatedError(VaccineError):
    """Raised when the visitor is not vaccinated."""
    pass

class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is expired."""
    pass

class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
    pass