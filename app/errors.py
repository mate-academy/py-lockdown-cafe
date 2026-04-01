class VaccineError(Exception):
    """Base class for Vaccine exceptions"""


class NotVaccinatedError(VaccineError):
    """Exception for situations where a person is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """Exception for situations where a person's vaccine is outdated'."""


class NotWearingMaskError(Exception):
    """Exception for situations where a person is not wearing the mask."""
