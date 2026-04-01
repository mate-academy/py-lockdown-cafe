class VaccineError(Exception):
    """Parent class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Exception raised when a visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Exception raised when a visitor has an outdated vaccine."""
    pass


class NotWearingMaskError(Exception):
    """Exception raised when a visitor didn't wear the mask."""
