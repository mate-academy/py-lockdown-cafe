class VaccineError(Exception):
    """Base class for exceptions related to vaccination."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Exception raised when a visitor is not wearing a mask."""
    pass
