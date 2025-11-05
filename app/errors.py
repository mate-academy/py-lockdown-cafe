class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when vaccine is outdated."""
    pass


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
    pass
