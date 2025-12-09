class VaccineError(Exception):
    """Base vaccine exception."""


class NotVaccinatedError(VaccineError):
    """Raised when a visitor has no vaccine."""


class OutdatedVaccineError(VaccineError):
    """Raised when vaccine is expired."""


class NotWearingMaskError(Exception):
    """Raised when visitor is not wearing a mask."""
