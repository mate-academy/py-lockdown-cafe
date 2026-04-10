class VaccineError(Exception):
    """Base class for vaccine errors."""


class NotVaccinatedError(VaccineError):
    """Raised when visitor is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Raised when vaccine is expired."""


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
