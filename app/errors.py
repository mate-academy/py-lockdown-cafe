class VaccineError(BaseException):
    """All quarantine violations"""


class NotVaccinatedError(VaccineError):
    """There is no vaccination."""


class OutdatedVaccineError(VaccineError):
    """The vaccination period has expired."""


class NotWearingMaskError(BaseException):
    """It is necessary to wear a protective mask."""
