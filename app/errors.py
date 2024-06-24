class VaccineError(Exception):
    """Base class for vaccine-related errors."""

    pass


class NotVaccinatedError(VaccineError):
    """Raised when the visitor is not vaccinated."""

    pass


class OutdatedVaccineError(VaccineError):
    """Raised when the vaccine is outdated."""

    pass


class NotWearingMaskError(Exception):
    """Raised when the visitor is not wearing a mask."""

    pass
