class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised when visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Exception raised when visitor is not wearing a mask."""
    pass
