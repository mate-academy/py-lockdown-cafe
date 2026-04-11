class VaccineError(Exception):
    """Father Error for errors"""
    pass


class NotVaccinatedError(VaccineError):
    """Raised when a user is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised when a user has old date of vaccine."""
    pass


class NotWearingMaskError(Exception):
    """Raised when a user is not wearing mask."""
    pass
