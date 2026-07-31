

class VaccineError(Exception):
    """Base class for exceptions in this module."""


class NotVaccinatedError(VaccineError):
    """Exception raised for errors in the input."""


class OutdatedVaccineError(VaccineError):
    """Exception raised for errors in the input."""


class NotWearingMaskError(Exception):
    """Exception raised for errors in the input."""
