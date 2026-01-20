class VaccineError(Exception):
    """Base class for exceptions related to the vaccine."""


class NotVaccinatedError(VaccineError):
    """Exception raised when the visitor does not have a vaccine."""


class OutdatedVaccineError(VaccineError):
    """Exception raised when the visitor's vaccine is outdated."""


class NotWearingMaskError(Exception):
    """Exception raised when the visitor is not wearing a mask."""
