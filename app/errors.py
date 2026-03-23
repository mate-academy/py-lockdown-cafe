class VaccineError(Exception):
    """Base class for all vaccine-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor has no vaccine record."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when the visitor's vaccine has expired."""
    pass


class NoExpirationDateError(VaccineError):
    """Raised when the vaccine record has no expiration date."""
    pass
