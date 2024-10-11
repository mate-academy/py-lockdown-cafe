class VaccineError(Exception):
    """Base class for vaccine errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when visitor has no vaccine."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when vaccine has been expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised when no mask on visitor."""
    pass
