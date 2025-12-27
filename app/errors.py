class VaccineError(Exception):
    """Base exception for vaccine-related issues."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has not been vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    pass
