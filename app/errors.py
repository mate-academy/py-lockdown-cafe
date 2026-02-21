class VaccineError(Exception):
    """Base class for exceptions in this module."""


class NotVaccinatedError(VaccineError):
    """Exception raised for not found errors."""


class OutdatedVaccineError(VaccineError):
    """Exception raised for outdated vaccine errors."""


class NotWearingMaskError(Exception):
    """Exception raised for not wearing mask errors."""
