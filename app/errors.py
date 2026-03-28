class VaccineError(Exception):
    """Base class for vaccine-related errors."""


class NotVaccinatedError(VaccineError):
    """Raised when a person is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Raised when a person's vaccine is outdated."""


class NotWearingMaskError(Exception):
    """Raised when a person not wearing a mask."""
