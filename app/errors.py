class VaccineError(Exception):
    """Parent exception for all vaccine-related issues."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    pass
