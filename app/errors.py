class VaccineError(Exception):
    """Base class for all vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor does not have a vaccine key."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
    pass
