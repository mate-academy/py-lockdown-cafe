class VaccineError(Exception):
    """Base class for vaccine related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when visitor has no vaccine."""


class OutdatedVaccineError(VaccineError):
    """Raised when vaccine is expired."""


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
