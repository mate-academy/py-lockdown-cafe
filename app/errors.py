class VaccineError(Exception):
    """Base exception for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
    pass
