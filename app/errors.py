class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor has no vaccine info."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
    pass
