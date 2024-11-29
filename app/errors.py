class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor is not vaccinated (no vaccine key)."""


class OutdatedVaccineError(VaccineError):
    """Raised when the vaccine is expired."""


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""
