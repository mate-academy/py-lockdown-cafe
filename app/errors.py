class VaccineError(Exception):
    """Base exception for vaccination-related errors."""
    pass


class NotVaccinatedError(VaccineError):
    """Raised if the visitor is not vaccinated."""
    pass


class OutdatedVaccineError(VaccineError):
    """Raised if the visitor's vaccine has expired."""
    pass


class NotWearingMaskError(Exception):
    """Raised if the visitor is not wearing a mask."""
    pass
