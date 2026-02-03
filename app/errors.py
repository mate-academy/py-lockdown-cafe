class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    """The visitor is not vaccinated."""


class OutdatedVaccineError(VaccineError):
    """The visitor has expired vaccine"""


class NotWearingMaskError(Exception):
    """The visitor must wear masks."""
