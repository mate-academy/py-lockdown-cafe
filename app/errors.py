class VaccineError(Exception):
    """Base class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor has no vaccine key."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when the vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
    pass
