class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
    pass


class VaccineError(Exception):
    """Base exception for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor does not have a vaccine."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine has expired."""
    pass
