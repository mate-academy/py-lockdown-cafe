class VaccineError(Exception):
    """Base class for vaccination related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine is outdated."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    pass
