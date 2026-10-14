class VaccineError(Exception):
    """Base class for all vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a visitor is not vaccinated (missing vaccine key)."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a visitor's vaccine expiration date has passed."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a visitor is not wearing a mask."""
    pass
