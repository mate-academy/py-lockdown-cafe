class VaccineError(Exception):
    """Parent class for vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor has no vaccine record."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine is expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
    pass
