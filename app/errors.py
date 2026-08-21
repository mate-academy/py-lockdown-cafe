"""Define exceptions raised when cafe admission rules are violated."""


class VaccineError(Exception):
    """Base exception for vaccine-related admission errors."""

    pass


class NotVaccinatedError(VaccineError):
    """Indicate that a visitor has no vaccine information."""

    pass


class OutdatedVaccineError(VaccineError):
    """Indicate that a visitor's vaccine has expired."""

    pass


class NotWearingMaskError(Exception):
    """Indicate that a visitor is not wearing a mask."""

    pass
