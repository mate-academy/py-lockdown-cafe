class VaccineError(Exception):
    """Base class for exceptions related to vaccines."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor does not have a vaccine key."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    pass
